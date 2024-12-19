from dotenv import load_dotenv
import os
from pymongo import MongoClient
load_dotenv()
#Pegando o link de um avariavel de ambiente
link = os.getenv("LINK_BD")
#Conectando com o bd MongoDB
client = MongoClient(link)
db = client["PythonVisualization"]
#Criando as coleções no mongo
collection = db["faturamento"]
collection2 = db["quantidade"]
collection3 = db["Ticket"]