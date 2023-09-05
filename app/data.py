from os import getenv

from certifi import where
from dotenv import load_dotenv
from MonsterLab import Monster
from pandas import DataFrame
from pymongo import MongoClient


class Database:

    def seed(self, amount):
        monsters = [Monster().to_dict() for _ in range(amount)]
        self.collection.insertMany(monsters)

    def reset(self):
        self.collection.deleteMany({})

    def count(self) -> int:
        pass

    def dataframe(self) -> DataFrame:
        pass

    def html_table(self) -> str:
        pass

    def __init__(self) -> None:
        load_dotenv()
        self.client = MongoClient(getenv("MONGO_URI"), tlsCAFile=where())
        self.db = self.client['Cluster0']
        self.collection = self.db['collection_name']