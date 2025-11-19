FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Instalar dependencias del sistema (opcional pero útil)
RUN apt-get update && apt-get install -y \
    build-essential \
 && rm -rf /var/lib/apt/lists/*

# Copiar archivo de dependencias
COPY app/requirements.txt /app/requirements.txt

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY app/ /app/

# Exponer el puerto interno donde escucha la app
EXPOSE 8000

# Comando para arrancar la app con gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
