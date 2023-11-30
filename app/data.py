from os import getenv
from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def __init__(self) -> None:
        load_dotenv()
        self.database = MongoClient(getenv("DB_URL"),
                                    tlsCAFile=where())["Database"]
        self.collection = self.database.get_collection("Monsters")

    def seed(self, amount):
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insert_many(monsters)

    def reset(self):
        self.collection.delete_many({})

    def count(self) -> int:
        return self.collection.count_documents({})

    def dataframe(self) -> DataFrame:
        return DataFrame(self.collection.find({}, {"_id": False}))

    def html_table(self) -> str:
        df = self.dataframe()
        if df.empty:
            return None
        return df.to_html()


if __name__ == '__main__':
    db = Database()
    db.reset()
