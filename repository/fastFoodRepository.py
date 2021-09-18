import pymongo

try:
    # Global dataBase connection
    conn = pymongo.MongoClient()
    db = conn.loja
except:
    print("DataBase connection error!")


def setDataBaseRepository(data):  # Set database with CSV File data if not exists

    dblist = conn.list_database_names()

    if "loja" not in dblist:
        collection = db.lojas  # create a collection called lojas

        collection.insert_many(data)  # inserting data in database

        print("Database created!")
    else:
        print("The database already exists.")
