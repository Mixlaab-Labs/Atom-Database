# Base de datos para el proyecto Atom
from pymongo import MongoClient
import datetime
from datetime import datetime

MONGO_URI='mongodb://localhost'

client = MongoClient(MONGO_URI)

db = client['dron']

collection = db['Giroscopio']
collection2 = db['Acelerometro']
collection3 = db['Consumo']

print('Inserte Aceleracion en cada eje (x,y,z):')
ax = input()
ay = input()
az = input()

print('Inserte datos del giroscopio (x,y,z):')
x = input()
y = input()
z = input()

print('Inserte bateria (%)y tiempo en vuelo (s):')
b = input()
t = input()

collection2.insert({'AX':ax,'AY':ay,'AZ':az, 'date':str(datetime.now())})
collection.insert({'X': x,'Y': y,'Z': z, 'date':str(datetime.now())})
bateria={'Bateria': b, 'date': str(datetime.now())}
tiempo={'Tiempo en vuelo': t, 'date':str(datetime.now())}
collection3.insert_many([bateria, tiempo])

Aceleracion=collection2.find()
for a in Aceleracion:
    print(a)

Giroscopio=collection.find()
for g in Giroscopio:
    print(g)

Consumo=collection3.find()
for c in Consumo:
    print(c)

print('Para borrar inserte 1, de lo contrario inserte cualquier otro valor:')
borrar = input()
if borrar==1:
    collection.delete_many({})
    collection2.delete_many({})
    collection3.delete_many({})
else: 
    exit()