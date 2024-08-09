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
car_data["manufacturer"] = car_data["manufacturer"].str.capitalize()
car_data["model"] = car_data["model"].str.split().str[1]

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

st.markdown("""
    <style>
    .h2{
        text-align: justified;
        font-size: 22px;
        font-family: 'Copperplate';
        color: #C1C9C2;
        }
    </style>
    <div class="h2">Primer página web donde se busca eficientar y automatizar el análisis de datos de una compañía de venta de coches. Se busca hacer uso de diferentes elementos tales como casillas de selección, botones y casillas de verificación, así como diferentes tipos de gráficas con datos relevantes para los usuarios.</div>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
    .h1{
        text-align: center;
        font-size: 35px;
        font-family: 'Copperplate';
        color: #C1C9C2;
        padding-bottom: 30px;
        padding-top: 50px;
        }
    </style>
    <div class="h1">Uso de casillas de verificación</div>
""", unsafe_allow_html=True)

car_data_top = car_data[car_data["price"]>=90000.0]
car_data_top = car_data_top.reset_index(drop=True)
car_data_top = car_data_top.reindex(["price", "manufacturer",
                                     "model", "model_year",
                                     "condition", "cylinders",
                                     "odometer", "transmission",
                                     "type", "fuel", "paint_color",
                                     "is_4wd", "date_posted", 
                                     "days_listed"
                                     ],
                                     axis=1)

car_data_0 = car_data[car_data["odometer"]==0]
car_data_0 = car_data_0.reset_index(drop=True)
car_data_0 = car_data_0.reindex(["price", "manufacturer",
                                "model", "model_year",
                                "condition", "cylinders",
                                "odometer", "transmission",
                                "type", "fuel", "paint_color",
                                "is_4wd", "date_posted", 
                                "days_listed"
                                ],
                                axis=1)

# Casilla de verificación con información relevante
table_button = st.checkbox("Mostrar tabla de los vehículos más caros")
table_button2 = st.checkbox("Mostrar tabla de los vehículos menos usados")

if table_button:
    st.write(
        "Los 20 vehículos más caros de la tienda")
    st.dataframe(car_data_top, use_container_width=True)
if table_button2:
    st.write(
        "Vehículos con 0 kilometraje")
    st.dataframe(car_data_0, use_container_width=True)

st.markdown("""
    <div class="h1">Uso de botones</div>
""", unsafe_allow_html=True)

# Botón de gráfica para la creación de gráfico de caja
col1, col2 = st.columns([2,1])
with col1:
    box_button = st.button("Construir un gráfico de caja")

if box_button:
    st.write(
        "Comparación entre el kilometraje y la condición del vehículo")
    fig = px.box(car_data, x='condition', y='odometer', color='condition', title='Condición vs Kilometraje')
    st.plotly_chart(fig, use_container_width=True)

# Botón de gráfica para la creación de gráfico de violin
with col2:
    vio_button = st.button("Construir un gráfico de violin")

if vio_button:
    st.write("Relación estre condición y año del vehículo")
    fig = px.violin(car_data, x='model_year', y='condition', color='condition',
                 title='Condición vs Año del Modelo')
    st.plotly_chart(fig, use_container_width=True)

st.markdown("""
    <div class="h1">Uso casillas de selección</div>
""", unsafe_allow_html=True)

# Comparación de precios entre coches de una marca
manufacturera = st.selectbox("Seleccione un fabricante:", car_data["manufacturer"].unique())

filtro = car_data[car_data["manufacturer"] == manufacturera]

if len(filtro) >= 2:
    modelo_1 = st.selectbox("Seleccione un vehículo:", filtro["model"].unique())
    modelo_2 = st.selectbox("Seleccione otro vehículo:", filtro["model"].unique())

    comp = filtro[filtro["model"].isin([modelo_1,modelo_2])]

    fig = px.histogram(comp, x='price', color='model', 
                       barmode='overlay', 
                       histnorm='probability density', title=f"Comparación de precios entre {manufacturera} {modelo_1} y {manufacturera} {modelo_2}")
    st.plotly_chart(fig, use_container_width=True)


# Comparación de días de rotación entre marcas
man1 = st.selectbox("Seleccione una compañía vehicular:", car_data["manufacturer"].unique())
man2 = st.selectbox("Seleccione otra compañía vehicular:", car_data["manufacturer"].unique())

if (car_data["manufacturer"].isin([man1]).any()) and (car_data["manufacturer"].isin([man2]).any()):

    filtro = car_data[car_data['manufacturer'].isin([man1, man2])]
    fig = px.histogram(filtro, x='days_listed', color="manufacturer", 
                       barmode='overlay', 
                       histnorm='probability density', title=f"Días de rotación entre {man1} y {man2}")
    st.plotly_chart(fig, use_container_width=True)
    
