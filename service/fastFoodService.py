# Essa classe pega os dados de um arquivo csv e coloca no banco de dados
import pandas as pd
import repository.fastFoodRepository as repo
from bson.objectid import ObjectId


def setRepository():  # Get data from CSV File

    try:

        df = pd.read_csv("src/Fast_Food_Restaurants_US.csv")

        # Ignoring first column (index)
        df.drop(columns=df.columns[0], inplace=True)

        lojasList = df.to_dict("records")

        # getting websites as list
        for loja in lojasList:
            loja.update({"websites": str(loja["websites"]).split(",")})

        # persisting in dataBase
        repo.setDataBaseRepository(
            lojasList
        )
    except:
        print("File not Found!")


def verifyColumns(dic):  # Check if fields are valids

    try:

        df = pd.read_csv("src/Fast_Food_Restaurants_US.csv")

        # Ignoring first column (index)
        df.drop(columns=df.columns[0], inplace=True)

        return df.to_dict().keys() == dic.keys()
    except:
        print("File not Found!")


def findAll():  # Returns all fast food instances
    obj = list(repo.db.lojas.find())
    for x in obj:
        x["_id"] = str(x["_id"])
    return obj


def findById(id):  # Returns fast food by id
    obj = repo.db.lojas.find_one({"_id": ObjectId(id)})
    obj["_id"] = str(obj["_id"])
    return obj


def save(obj):  # Saves a fast food instance and returns created body
    obj = str(repo.db.lojas.insert_one(obj).inserted_id)
    return findById(obj)


def delete(id):  # Delete a fast food instance and returns deleted body
    old = findById(id)
    repo.db.lojas.delete_one({"_id": ObjectId(id)})
    return old


def update(id, novo):  # Update a fast food instance and returns updated body

    obj = repo.db.lojas.update_one({"_id": ObjectId(id)}, {
        "$set": novo}).raw_result

    return findById(id)
