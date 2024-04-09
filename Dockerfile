# Usa la imagen base de Python
FROM python:3.9-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Instala las dependencias
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copia los archivos necesarios al contenedor
COPY ./app .

# Expón el puerto 8000
EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]