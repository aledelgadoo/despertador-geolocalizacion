import streamlit as st
import folium
from streamlit_folium import st_folium

# Titulos y texto que se mostrará en la página web
st.title("⏰ Despertador por geolocalización")

st.title("Mapa básico con Folium")

# Definimos una ubicación central
ubicacion_central = [28.1235, -15.4366]

# Creamos el mapa centrado en esa ubicación
mapa = folium.Map(location=ubicacion_central, zoom_start=13)

# Ponemos un marcador en esa ubicación
folium.Marker(
    location=ubicacion_central,
    tooltip="Aquí estoy",
    icon=folium.Icon(color="red", icon="home")
).add_to(mapa)

# Mostramos el mapa en Streamlit
st_data = st_folium(mapa, width=700, height=500)