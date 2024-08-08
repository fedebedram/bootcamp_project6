# Importación de librerías
import pandas as pd
import plotly.express as px
import streamlit as st

# Importación del df
car_data = pd.read_csv("vehicles_us.csv")

# Limpieza del df, justificación en /notebook/
car_data["is_4wd"] = car_data["is_4wd"].replace(1., "4wd")
car_data["is_4wd"] = car_data["is_4wd"].fillna("2wd")
car_data["model_year"] = car_data["model_year"].astype("Int64")
car_data["cylinders"] = car_data["cylinders"].astype("Int64")
car_data["odometer"] = car_data["odometer"].astype("Int64")
car_data["date_posted"] = pd.to_datetime(
    car_data["date_posted"], format="%Y-%m-%d")
car_data["price"] = car_data["price"].astype("float")
car_data["manufacturer"] = car_data["model"].str.split().str[0]

# Título de la página web
st.markdown("""
    <style>
    .header{
        text-align: center;
        font-size: 60px;
        font-family: 'Copperplate';
        color: #C1C9C2;
        font-weight: italic;
        padding-bottom: 50px;
        }
    </style>
    <div class="header">Análisis vehicular</div>
""", unsafe_allow_html=True)

# Casilla de verificación con información relevante
table_button = st.checkbox("Tabla de...")
211
if table_button:
    st.write(
        "Creación de histograma con la dispersión del kilometraje de los vehículos")

# Botón de gráfica para la creación del histograma
hist_button = st.button("Construir un histograma")

if hist_button:
    st.write(
        "En construcción...")
    fig = px.histogram(
        car_data,
        x="odometer"
    )
    st.plotly_chart(fig, use_container_width=True)

# Botón de gráfica para la creación del histograma
scat_button = st.button("Construir un gráfico de dispersión")

if scat_button:
    st.write("En construcción...")
    fig = px.scatter(
        car_data,
        x="odometer",
        y="price"
    )
    st.plotly_chart(fig, use_container_width=True)