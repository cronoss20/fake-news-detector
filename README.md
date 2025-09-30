# Fake News Detector

Este repositorio contiene un proyecto para detectar noticias falsas utilizando varios algoritmos y conjuntos de datos.

## Requisitos

- Python 3.9+ (si se ejecuta localmente)
- Docker (opcional)
- Clave de API de OpenAI (necesaria para el funcionamiento del modelo)

## Instalación local

1. Clona el repositorio:
   ```bash
   git clone https://github.com/cronoss20/fake-news-detector.git
   cd fake-news-detector
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura las variables de entorno:

   Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido (reemplaza `TU_API_KEY` con tu clave real):

   ```
   OPENAI_API_KEY=TU_API_KEY
   ```

## Ejecución local

Ejecuta la aplicación con:

```bash
python app.py
```

La aplicación estará disponible en http://localhost:5000.

## Uso con Docker

1. Construye la imagen:

   ```bash
   docker build -t fake-news-detector .
   ```

2. Ejecuta el contenedor, asegurándote de pasar el archivo `.env`:

   ```bash
   docker run --env-file .env -p 5000:5000 fake-news-detector
   ```

La aplicación estará disponible en http://localhost:5000.

## Estructura del repositorio

- `app.py`: Código principal de la aplicación backend.
- `frontend/`: Carpeta reservada para el frontend (si aplica).
- `requirements.txt`: Dependencias de Python.
- `Dockerfile`: Para construir la imagen Docker.
- `.env`: Variables de entorno (no se debe compartir en público).

## Notas

- Asegúrate de tener una clave válida de OpenAI para usar el detector.
- Para desarrollo o personalización, añade tus propios algoritmos/datasets en la estructura actual.

---

Siente libre de contribuir o abrir issues para mejoras.
