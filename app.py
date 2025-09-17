import pandas as pd
import plotly.graph_objects as go  # Usaremos graph_objects para los gráficos
import streamlit as st

# --- Configuración de la página ---
st.set_page_config(page_title="Sprint 7 - Streamlit Demo", layout="wide")

# --- Encabezado ---
st.header("Anuncios de venta de coches — Sprint 7")

# --- Cargar datos ---


@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """Lee el CSV y devuelve un DataFrame"""
    return pd.read_csv(path)


try:
    car_data = load_data("vehicles_us.csv")
    st.write("Vista del dataset (primeras filas):")
    st.write(car_data.head())
except FileNotFoundError:
    st.error(
        "No se encontró 'vehicles_us.csv' en la raíz del proyecto. Colócalo y recarga la app.")
    st.stop()

# --- Botón para histograma ---
hist_button = st.button("Construir histograma (odometer)")
if hist_button:
    st.write("Creación de un histograma para la columna 'odometer'")
    fig = go.Figure(data=[go.Histogram(x=car_data["odometer"])])
    fig.update_layout(
        title_text="Distribución del odómetro",
        xaxis_title="Odómetro",
        yaxis_title="Frecuencia"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- Botón para gráfico de dispersión ---
scatter_button = st.button(
    "Construir gráfico de dispersión (odometer vs price)")
if scatter_button:
    st.write("Creación de un gráfico de dispersión para 'odometer' vs 'price'")
    fig2 = go.Figure(
        data=[go.Scatter(
            x=car_data["odometer"],
            y=car_data["price"],
            mode="markers",
            opacity=0.6
        )]
    )
    fig2.update_layout(
        title_text="Relación entre odómetro y precio",
        xaxis_title="Odómetro",
        yaxis_title="Precio"
    )
    st.plotly_chart(fig2, use_container_width=True)
