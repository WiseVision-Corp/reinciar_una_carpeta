import shutil
import datetime

ruta_archivo = "/ruta/del/archivo/a/reiniciar"  # Reemplaza con la ruta del archivo que deseas reiniciar
ruta_log = "/ruta/del/archivo.log"  # Reemplaza con la ruta del archivo de log donde deseas guardar los datos de reinicio

# Fecha y hora actual
fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Reiniciar el archivo
shutil.copy(ruta_archivo, f"{ruta_archivo}.bak")  # Hacer una copia de seguridad del archivo original
open(ruta_archivo, "w").close()  # Vaciar el archivo original

# Guardar los datos de reinicio en el log
with open(ruta_log, "a") as log_file:
    log_file.write(f"Archivo reiniciado el {fecha_actual}\n")

print("Archivo reiniciado exitosamente.")


# crontab -e  //Se abrirá el archivo de tareas programadas en el editor predeterminado. 
# Agrega una nueva línea al final del archivo para programar la ejecución del script en la fecha y hora deseada.
# 0 0 * * * python3 /ruta/del/reiniciar_archivo.py En este ejemplo, el script se ejecutará todos los días a las 12:00 a.m. (medianoche).
# ajustar la programación de acuerdo a tus necesidades utilizando la sintaxis de cron.