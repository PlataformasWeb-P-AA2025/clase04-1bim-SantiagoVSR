import csv
import json
import uuid

# Ruta del archivo CSV de entrada y del JSON de salida
archivo_csv = 'atp_tennis.csv'
archivo_json = 'atp_tennis_couchdb.json'

# Leer el archivo CSV
with open(archivo_csv, newline='', encoding='latin1') as csvfile:
    lector = csv.DictReader(csvfile)
    documentos = []

    for fila in lector:
        # Generar un UUID como _id para CouchDB
        doc = {'_id': str(uuid.uuid4())}
        # Agregar el resto de los campos del CSV al documento
        doc.update(fila)
        documentos.append(doc)

# Guardar la lista de documentos como JSON
with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
    json.dump(documentos, jsonfile, indent=4, ensure_ascii=False)

print(f'Archivo JSON creado exitosamente: {archivo_json}')
