#!/bin/bash

ruta_directorio="/monit/IBM/tivoli/impact"  # Ruta del directorio a respaldar
ruta_respaldo="/monit/IBM/tivoli/carpeta_respaldo"  # Ruta del directorio de respaldo donde se guardarán los archivos
ruta_log="/monit/IBM/tivoli/log-respaldo.txt"  # Ruta del archivo de log para guardar los datos de reinicio y respaldo

# Fecha y hora actual
fecha_actual=$(date +"%Y-%m-%d %H:%M:%S")

# Comprobar si el directorio de respaldo existe, si no, crearlo
if [ ! -d "$ruta_respaldo" ]; then
  mkdir -p "$ruta_respaldo"
fi

# Verificar si la carpeta de logs existe, si no, crearla
if [ ! -d "$(dirname "$ruta_log")" ]; then
  mkdir -p "$(dirname "$ruta_log")"
fi

# Formatear el nombre de la carpeta de respaldo
nombre_respaldo="respaldo_$(date +"%Y-%m-%d_%H-%M-%S")"
ruta_respaldo_fecha="${ruta_respaldo}/${nombre_respaldo}"

# Crear una copia de respaldo de los archivos y carpetas dentro de la carpeta1
cp -r "${ruta_directorio}" "${ruta_respaldo_fecha}" >> "${ruta_log}" 2>&1

# Comprimir la copia de respaldo en un archivo tar.gz
tar -czf "${ruta_respaldo}/${nombre_respaldo}.tar.gz" -C "${ruta_respaldo}" "${nombre_respaldo}" >> "${ruta_log}" 2>&1

# Eliminar la carpeta de respaldo sin comprimir
rm -r "${ruta_respaldo_fecha}" >> "${ruta_log}" 2>&1

# Guardar los datos de reinicio en el log
echo "Directorio reiniciado y respaldado el ${fecha_actual}" >> "${ruta_log}"

# Vaciar el contenido de la carpeta1
rm -r "${ruta_directorio}"/* >> "${ruta_log}" 2>&1


echo "Directorio reiniciado y respaldado exitosamente."

