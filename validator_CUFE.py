import fitz  # PyMuPDF
from pyzbar.pyzbar import decode
from PIL import Image
import re
import os
import sqlite3

# Ruta de la carpeta que contiene los archivos PDF
folder_path = r"C:\ProjectAdresPythonCUFE\facturas"

# Configuración de la base de datos
conn = sqlite3.connect('facturas.db')
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute('''CREATE TABLE IF NOT EXISTS facturas (
                   nombre_archivo TEXT,
                   numero_paginas INTEGER,
                   CUFE TEXT,
                   peso_archivo REAL)''')
conn.commit()

def extract_qr_from_pdf(pdf_path):
    # Obtiene el nombre y peso del archivo
    nombre_archivo = os.path.basename(pdf_path)
    peso_archivo = os.path.getsize(pdf_path) / 1024  # Peso en KB

    # Abre el archivo PDF y cuenta las páginas
    pdf_document = fitz.open(pdf_path)
    numero_paginas = pdf_document.page_count
    cufe = None

    # Recorre todas las páginas del PDF
    for page_num in range(numero_paginas):
        page = pdf_document.load_page(page_num)
        
        # Incrementa la resolución de la imagen
        zoom = 2  # Cambiar el valor para mejorar la resolución
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        
        # Decodifica el QR
        qr_codes = decode(img)
        
        for qr in qr_codes:
            qr_data = qr.data.decode("utf-8")
            print("QR Data encontrado:", qr_data)  # Para depuración
            
            # Extrae el CUFE de la URL
            match = re.search(r"documentkey=([a-zA-Z0-9]+)", qr_data)
            if match:
                cufe = match.group(1)
                print("CUFE:", cufe)
                
                # Verifica si el CUFE cumple con la expresión regular
                if re.fullmatch(r"(\b([0-9a-fA-F]\n*){95,100}\b)", cufe):
                    print("El CUFE cumple con la expresión regular.")
                else:
                    print("El CUFE NO cumple con la expresión regular.")
                
                break
        if cufe:
            break  # Sale del bucle si se encontró el CUFE

    # Inserta la información en la base de datos
    cursor.execute('INSERT INTO facturas (nombre_archivo, numero_paginas, CUFE, peso_archivo) VALUES (?, ?, ?, ?)',
                   (nombre_archivo, numero_paginas, cufe, peso_archivo))
    conn.commit()
    print(f"Datos almacenados: {nombre_archivo}, {numero_paginas} páginas, CUFE: {cufe}, {peso_archivo:.2f} KB")

    pdf_document.close()

# Procesa cada archivo PDF en la carpeta
for filename in os.listdir(folder_path):
    if filename.endswith(".pdf") or filename.endswith(".PDF"):
        pdf_path = os.path.join(folder_path, filename)
        extract_qr_from_pdf(pdf_path)

conn.close()
