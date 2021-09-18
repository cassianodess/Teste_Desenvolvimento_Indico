# Essa classe pega os dados de um arquivo csv e coloca no banco de dados
import pandas as pd
import pymongo
from bson.objectid import ObjectId

conn = pymongo.MongoClient()
db = conn.loja


def setDataBaseRepository(data):

    collection = db.lojas

    collection.insert_many(data)


def setRepository():
    df = pd.read_csv(
        "repository/Fast_Food_Restaurants_US.csv")

    df.drop(columns=df.columns[0], inplace=True)

    setDataBaseRepository(
        df.to_dict("records")
    )


def findAll():
    obj = list(db.lojas.find())
    for x in obj:
        x["_id"] = str(x["_id"])
    return obj


def findById(id):
    obj = db.lojas.find_one({"_id": ObjectId(id)})
    obj["_id"] = str(obj["_id"])
    return obj


def save(obj):
    obj = str(db.lojas.insert_one(obj).inserted_id)
    return findById(obj)


def delete(id):
    old = findById(id)
    db.lojas.delete_one({"_id": ObjectId(id)})
    return old


def update(id, novo):

    obj = db.lojas.update_one({"_id": ObjectId(id)}, {
                              "$set": novo}).raw_result

    return findById(id)
