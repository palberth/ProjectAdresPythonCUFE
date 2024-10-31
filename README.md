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

Coloca los archivos PDF que deseas procesar en la carpeta especificada en el script ("C:\ProjectAdresPythonCUFE\facturas") o modifica la variable folder_path en el script para apuntar a la ruta deseada.

Ejecuta el script:

    ```bash
    python pdf_qr_extractor.py


