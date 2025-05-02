import requests
import json

# Ruta del archivo JSON generado
ruta_json = '/home/santiago/Escritorio/web/semana04/clase04-1bim-SantiagoVSR/ejemplo05/atp_tennis_couchdb.json'

# Cargar los datos desde el archivo JSON
with open(ruta_json, 'r') as f:
    data = json.load(f)

lista_datos = []

for d in data['docs']:
    if d['Tournament'][0] in ["A", "B", "L"]:
        lista_datos.append(d)


# Nombre de la base de datos en CouchDB (debe existir previamente)
base_datos = "atp_tennis001"

# URL de CouchDB (ajústala si usas usuario/contraseña o IP distinta)
url = f"http://127.0.0.1:5984/{base_datos}/_bulk_docs"
headers = {'Content-Type': 'application/json'}

# Preparar los datos en formato {"docs": [...]}
datos_finales = {'docs': lista_datos}

# Enviar los datos a CouchDB
response = requests.post(url, headers=headers, json=datos_finales)

# Mostrar respuesta del servidor
print("Código de estado:", response.status_code)
print("Respuesta:", response.json())
