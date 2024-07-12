from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Obtener la URI de conexión de las variables de entorno
uri = os.getenv('MONGODB_URI')

# Crear una instancia del cliente de MongoDB
client = MongoClient(uri, serverSelectionTimeoutMS=5000)

# Datos de las provincias dominicanas
provincias = [
    {'nombre': 'Azua', 'region': 'Sur'},
    {'nombre': 'Baoruco', 'region': 'Sur'},
    {'nombre': 'Barahona', 'region': 'Sur'},
    {'nombre': 'Dajabón', 'region': 'Noroeste'},
    {'nombre': 'Distrito Nacional', 'region': 'Ozama'},
    {'nombre': 'Duarte', 'region': 'Nordeste'},
    {'nombre': 'Elías Piña', 'region': 'Sur'},
    {'nombre': 'El Seibo', 'region': 'Este'},
    {'nombre': 'Espaillat', 'region': 'Norte'},
    {'nombre': 'Hato Mayor', 'region': 'Este'},
    {'nombre': 'Hermanas Mirabal', 'region': 'Nordeste'},
    {'nombre': 'Independencia', 'region': 'Sur'},
    {'nombre': 'La Altagracia', 'region': 'Este'},
    {'nombre': 'La Romana', 'region': 'Este'},
    {'nombre': 'La Vega', 'region': 'Norte'},
    {'nombre': 'María Trinidad Sánchez', 'region': 'Nordeste'},
    {'nombre': 'Monseñor Nouel', 'region': 'Norte'},
    {'nombre': 'Monte Cristi', 'region': 'Noroeste'},
    {'nombre': 'Monte Plata', 'region': 'Ozama'},
    {'nombre': 'Pedernales', 'region': 'Sur'},
    {'nombre': 'Peravia', 'region': 'Sur'},
    {'nombre': 'Puerto Plata', 'region': 'Norte'},
    {'nombre': 'Samaná', 'region': 'Nordeste'},
    {'nombre': 'San Cristóbal', 'region': 'Ozama'},
    {'nombre': 'San José de Ocoa', 'region': 'Sur'},
    {'nombre': 'San Juan', 'region': 'Sur'},
    {'nombre': 'San Pedro de Macorís', 'region': 'Este'},
    {'nombre': 'Sánchez Ramírez', 'region': 'Norte'},
    {'nombre': 'Santiago', 'region': 'Norte'},
    {'nombre': 'Santiago Rodríguez', 'region': 'Noroeste'},
    {'nombre': 'Santo Domingo', 'region': 'Ozama'},
    {'nombre': 'Valverde', 'region': 'Noroeste'}
]

# Función principal
def main():
    try:
        # Conectar al cliente
        client.server_info()  # Esto es para forzar una conexión y verificarla

        # Conectarse a la base de datos
        database = client['provincias']
        collection = database['provincias']

        # Inserta los datos en la colección
        collection.insert_many(provincias)
        print('Datos insertados correctamente')

        # Recupera e imprime los datos
        results = collection.find({})
        print('Datos en la colección:')
        for result in results:
            print(result)
    except Exception as error:
        print('Error:', error)
    finally:
        # Cierra la conexión del cliente
        client.close()

# Ejecuta la función principal
if __name__ == '__main__':
    main()
