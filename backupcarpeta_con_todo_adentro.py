
import shutil
import datetime
import os

ruta_directorio = "./carpeta"  # Ruta del directorio a reiniciar y respaldar
ruta_respaldo = "./carpeta_respaldo"  # Ruta del directorio de respaldo donde se guardarán los archivos
ruta_log = "./logs"  # Ruta del archivo de log para guardar los datos de reinicio y respaldo

# Fecha y hora actual
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Crear una copia de respaldo del directorio y sus archivos
ruta_respaldo_fecha = os.path.join(ruta_respaldo, fecha_actual)
shutil.copytree(ruta_directorio, ruta_respaldo_fecha)

# Vaciar el directorio original y eliminar sus archivos
for root, dirs, files in os.walk(ruta_directorio):
    for file in files:
        os.remove(os.path.join(root, file))

# Guardar los datos de reinicio en el log
with open(ruta_log, "a") as log_file:
    log_file.write(f"Directorio reiniciado y respaldado el {fecha_actual}\n")

print("Directorio reiniciado y respaldado exitosamente.")