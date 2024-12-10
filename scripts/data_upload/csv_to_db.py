import sqlite3
import os
import pandas as pd
from pandas import read_csv

db_location = r"C:\Users\daini\PycharmProjects\CodeAcademy\CarService\db.sqlite3"

conn = sqlite3.connect(db_location)
cursor = conn.cursor()


#1 autoservice_app_Automobilio_modelis
data_location = r"C:\Users\daini\OneDrive\Desktop\BD\autoservice_app_Automobilio_modelis.csv"
auto_data = pd.read_csv(data_location, sep=",")
auto_data.to_sql('carservice_carmodel', conn, if_exists="append", index=False)


#2 autoservice_app_paslauga
data_location = r"C:\Users\daini\OneDrive\Desktop\BD\autoservice_app_paslauga.csv"
auto_data = pd.read_csv(data_location, sep=",")
auto_data.to_sql('carservice_service', conn, if_exists="append", index=False)


#3 autoservice_app_automobilis
data_location = r"C:\Users\daini\OneDrive\Desktop\BD\autoservice_app_automobilis.csv"
auto_data = pd.read_csv(data_location, sep=",")
auto_data.to_sql('carservice_automobile', conn, if_exists="append", index=False)


#4 autoservice_app_uzsakymas
data_location = r"C:\Users\daini\OneDrive\Desktop\BD\autoservice_app_uzsakymas.csv"
auto_data = pd.read_csv(data_location, sep=",")
auto_data.to_sql('carservice_order', conn, if_exists="append", index=False)


#5 autoservice_app_Uzsakymo_eilute
data_location = r"C:\Users\daini\OneDrive\Desktop\BD\autoservice_app_Uzsakymo_eilute.csv"
auto_data = pd.read_csv(data_location, sep=",")
auto_data.to_sql('carservice_serviceorder', conn, if_exists="append", index=False)

conn.close()