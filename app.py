# Importación de librerías
import pandas as pd
import plotly.express as ps
import streamlit as st

# Importación del df
car_data = pd.read_csv(
    "/Users/federicobedollaramos/Desktop/TripleTen/Sprint 6/Proyecto/bootcamp_project6/vehicles_us.csv")

# Limpieza del df, justificación en /notebook/
car_data["is_4wd"] = car_data["is_4wd"].replace(1., "4wd")
car_data["is_4wd"] = car_data["is_4wd"].fillna("2wd")
car_data["model_year"] = car_data["model_year"].astype("Int64")
car_data["cylinders"] = car_data["cylinders"].astype("Int64")
car_data["odometer"] = car_data["odometer"].astype("Int64")
car_data["date_posted"] = pd.to_datetime(
    car_data["date_posted"], format="%Y-%m-%d")
