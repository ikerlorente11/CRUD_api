#!/bin/bash

# Ejecutar migraciones de la base de datos
flask db upgrade

# Iniciar la aplicación FastAPI con Uvicorn
uvicorn app.main:app --host 0.0.0.0 --port $PORT