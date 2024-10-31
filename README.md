# PDF QR Extractor to SQLite

Este proyecto permite extraer el `CUFE` de los códigos QR en archivos PDF en una carpeta específica y almacenar la información en una base de datos SQLite. Incluye detalles como el nombre del archivo, número de páginas, `CUFE` y peso del archivo.

## Requisitos

- Python 3.7 o superior
- Las librerías necesarias se encuentran en el archivo `requirements.txt`.

## Instalación

1. **Clona el repositorio** (o descarga los archivos manualmente):

   ```bash
   git clone https://github.com/tu-usuario/pdf_qr_extractor.git
   cd pdf_qr_extractor

2. **Instalar dependencias**

    Instala las dependencias listadas en requirements.txt:
    ```bash
    pip install -r requirements.txt

## Uso

Coloca los archivos PDF que deseas procesar en la carpeta especificada en el script ("C:\ProjectAdresPythonCUFE\facturas") o modifica la variable folder_path en el script para apuntar a la ruta deseada y Ejecuta el script:
    
    
    python pdf_qr_extractor.py

El script recorrerá cada archivo PDF en la carpeta y extraerá la siguiente información:

- Nombre del archivo
- Número de páginas
- CUFE
- Peso del archivo (en KB)

Toda esta información se almacenará en una base de datos SQLite llamada facturas.db.

## Notas

Asegúrate de que los archivos PDF contienen códigos QR con el parámetro documentkey en la URL, ya que el script busca específicamente ese valor.
La base de datos SQLite se crea en el mismo directorio y se llama facturas.db.

## Dependencias

- PyMuPDF (fitz): Para leer y procesar archivos PDF.
- pyzbar: Para decodificar los códigos QR de las imágenes.
- Pillow: Para manejar la conversión de PDF a imagen.

## Contribuir

Si deseas contribuir al proyecto, realiza un fork, crea una nueva rama con tus cambios y envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.