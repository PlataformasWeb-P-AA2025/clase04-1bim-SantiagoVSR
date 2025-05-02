import requests
import json

# Cargar la lista de documentos
with open('/home/santiago/Escritorio/web/semana04/clase04-1bim-SantiagoVSR/ejemplo05/atp_tennis_couchdb.json', 'r') as f:
    data = json.load(f)  # Lista de documentos


lista_datos = []

for d in data['docs']:
    if d['Tournament'][0] in ["A", "B", "L"]:
        lista_datos.append(d)

# Nombre de la base de datos
base_datos = "atp_tennis002"
url = f"http://127.0.0.1:5984/{base_datos}"
headers = {'Content-Type': 'application/json'}

# Insertar documentos uno por uno (como en tu código original)
for doc in lista_datos:
    response = requests.post(url, headers=headers, json=doc)
    estado = response.status_code
    resultado = response.json()
    print(f"Insertando ID {doc['_id']} | Estado: {estado} | Resultado: {resultado}")
