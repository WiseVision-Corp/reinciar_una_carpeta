ruta_directorio="~/reinciar_una_carpeta/carpeta"  # Ruta del directorio a reiniciar y respaldar
ruta_respaldo="~/reinciar_una_carpeta/carpeta_respaldo"  # Ruta del directorio de respaldo donde se guardarán los archivos
ruta_log="~/reinciar_una_carpeta/logs/log.txt"  # Ruta del archivo de log para guardar los datos de reinicio y respaldo

# Fecha y hora actual
fecha_actual=$(date +"%Y-%m-%d %H:%M:%S")

# Crear una copia de respaldo del directorio y sus archivos
ruta_respaldo_fecha="${ruta_respaldo}/${fecha_actual//:/-}"
ruta_respaldo_fecha="${ruta_respaldo_fecha// /_}"
cp -r "${ruta_directorio}" "${ruta_respaldo_fecha}"

# Comprimir la copia de respaldo en un archivo tar.gz
tar -czf "${ruta_respaldo_fecha}.tar.gz" "${ruta_respaldo_fecha}"

# Eliminar la carpeta de respaldo sin comprimir
rm -r "${ruta_respaldo_fecha}"

# Vaciar el directorio original y eliminar sus archivos
find "${ruta_directorio}" -type f -delete

# Guardar los datos de reinicio en el log
echo "Directorio reiniciado y respaldado el ${fecha_actual}" >> "${ruta_log}"

echo "Directorio reiniciado y respaldado exitosamente."
