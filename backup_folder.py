import shutil
import datetime
import os
import tarfile
import traceback



def backup_folder(source_folder, target_folder, log_file):
    try:
        # Fecha y hora actual
        fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Crear una copia de respaldo del directorio y sus archivos
        ruta_respaldo_fecha = os.path.join(target_folder, fecha_actual.replace(":", "-").replace(" ", "_"))
        shutil.copytree(source_folder, ruta_respaldo_fecha)

        # Comprimir la copia de respaldo en un archivo tar.gz
        backup_file = os.path.join(target_folder, f"backup_{fecha_actual.replace(':', '-')}.tar.gz")
        with tarfile.open(backup_file, "w:gz") as tar:
            tar.add(ruta_respaldo_fecha, arcname=os.path.basename(ruta_respaldo_fecha))

        # Vaciar el directorio original y eliminar sus archivos
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                os.remove(os.path.join(root, file))

        # Guardar los datos de reinicio en el log
        with open(log_file, "a") as log:
            log.write(f"Directorio reiniciado y respaldado el {fecha_actual}\n")

        print("Directorio reiniciado y respaldado exitosamente.")

    except Exception as e:
        # Registrar la excepción y el traceback en el archivo de log
        with open(log_file, "a") as log:
            log.write("Ocurrió un error en el script:\n")
            log.write(traceback.format_exc())
        raise e




ruta_directorio = "C:\\Users\\luist\\OneDrive\\Escritorio\\reinciar_una_carpeta\\carpeta"
ruta_respaldo = "C:\\Users\\luist\\OneDrive\\Escritorio\\reinciar_una_carpeta\\carpeta_respaldo"
ruta_log = "C:\\Users\\luist\\OneDrive\\Escritorio\\reinciar_una_carpeta\\logs\\log.txt"

backup_folder(ruta_directorio, ruta_respaldo, ruta_log)
