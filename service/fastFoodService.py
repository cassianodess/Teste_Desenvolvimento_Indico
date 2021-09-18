# Essa classe pega os dados de um arquivo csv e coloca no banco de dados
import pandas as pd
import pymongo
from bson.objectid import ObjectId

# Global dataBase connection
conn = pymongo.MongoClient()
db = conn.loja


def setDataBaseRepository(data):  # Set database with CSV File data if not exists

    dblist = conn.list_database_names()

    if "loja" not in dblist:
        collection = db.lojas  # create a collection called lojas

        collection.insert_many(data)  # inserting data in database

        print("Database created!")
    else:
        print("The database already exists.")


def setRepository():  # Get data from CSV File
    df = pd.read_csv("service/Fast_Food_Restaurants_US.csv")

    # Ignoring first column (index)
    df.drop(columns=df.columns[0], inplace=True)

    # sending as a dict
    setDataBaseRepository(
        df.to_dict("records")
    )


def verifyColumns(dic):  # Check if fields are valids

    df = pd.read_csv("service/Fast_Food_Restaurants_US.csv")

    # Ignoring first column (index)
    df.drop(columns=df.columns[0], inplace=True)

    return df.to_dict().keys() == dic.keys()


def findAll():  # Returns all fast food instances
    obj = list(db.lojas.find())
    for x in obj:
        x["_id"] = str(x["_id"])
    return obj


def findById(id):  # Returns fast food by id
    obj = db.lojas.find_one({"_id": ObjectId(id)})
    obj["_id"] = str(obj["_id"])
    return obj


def save(obj):  # Saves a fast food instance and returns created body
    obj = str(db.lojas.insert_one(obj).inserted_id)
    return findById(obj)


def delete(id):  # Delete a fast food instance and returns deleted body
    old = findById(id)
    db.lojas.delete_one({"_id": ObjectId(id)})
    return old


def update(id, novo):  # Update a fast food instance and returns updated body

    obj = db.lojas.update_one({"_id": ObjectId(id)}, {
                              "$set": novo}).raw_result

    return findById(id)
