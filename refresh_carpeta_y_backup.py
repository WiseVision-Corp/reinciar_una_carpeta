import shutil
import datetime

ruta_directorio = "/ruta/del/directorio/a/reiniciar"  # Reemplaza con la ruta del directorio que deseas reiniciar y respaldar
ruta_respaldo = "/ruta/del/directorio_de_respaldo"  # Reemplaza con la ruta del directorio de respaldo donde deseas guardar los archivos

# Fecha y hora actual
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Crear una copia de respaldo del directorio
ruta_respaldo_fecha = f"{ruta_respaldo}/{fecha_actual}"
shutil.copytree(ruta_directorio, ruta_respaldo_fecha)

# Vaciar el directorio original
shutil.rmtree(ruta_directorio)
shutil.os.mkdir(ruta_directorio)

# Guardar los datos de reinicio en el log
ruta_log = "/ruta/del/archivo.log"  # Reemplaza con la ruta del archivo de log donde deseas guardar los datos de reinicio
with open(ruta_log, "a") as log_file:
    log_file.write(f"Directorio reiniciado y respaldado el {fecha_actual}\n")

print("Directorio reiniciado y respaldado exitosamente.")