import os
import subprocess

# Ejecuta el comando `flask db upgrade` antes de iniciar el servidor
subprocess.run(["flask", "db", "upgrade"])

# Ahora inicia tu aplicación FastAPI con Uvicorn
os.system("uvicorn app.main:app --host 0.0.0.0 --port $PORT")