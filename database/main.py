from connection import MongoDBConnection
from repository import Property
from config import DB_USER, DB_PASSWORD, DB_CLUSTER , DB_URI

# Environment variables 
# DB_USER = os.environ['MONGO_DB_USER']
# DB_PASSWORD = os.environ['MONGO_DB_PASS']
# DB_CLUSTER = 'cluster0.mhq2j'
# DB_URI = f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_CLUSTER}.mongodb.net/"


if __name__ == "__main__":
    connection = MongoDBConnection(DB_URI)
    client = connection.connect()
    property_manager = Property(client)

    test_data = [
        {
            "state": "DF",
            "city": "Brasília",
            "description": "SHS Quadra 06 Conjunto A Bloco D, ASA SUL, BRASILIA",
            "type": "Aluguel Loja 86 m²",
            "price": 10.285,
            "size": 86,
            "bedrooms": None,
            "cars_spaces": None,
        },
        {
            "state": "SP",
            "city": "São Paulo",
            "description": "Av. Paulista, Bela Vista",
            "type": "Venda Apartamento 120 m²",
            "price": 1.250,
            "size": 120,
            "bedrooms": 3,
            "cars_spaces": 2,
        },
        {
            "state": "RJ",
            "city": "Rio de Janeiro",
            "description": "Rua Barata Ribeiro, Copacabana",
            "type": "Venda Apartamento 80 m²",
            "price": 900,
            "size": 80,
            "bedrooms": 2,
            "cars_spaces": 1,
        }
    ]

    inserted_ids = property_manager.insert_multiple_properties(test_data)
    print(f"Properties inserted with IDs: {inserted_ids}")

    connection.close()