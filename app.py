import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# Titulos y texto que se mostrará en la página web
st.title("⏰ Despertador por geolocalización")
st.title("Mapa básico con Folium")

# Creamos un slider para la longitud y latitud actual
# slider -> ("Texto que verá el usuario", valor min, valor max, valor por defecto, precisión)
lat_actual = st.slider("Latitud actual", 28.0, 28.3, 28.10, 0.0001)
lon_actual = st.slider("Longitud actual", -15.6, -15.3, -15.43, 0.0001)
pos_actual = (lat_actual, lon_actual)

radio_alarma = 500 # metros

# Creamos el mapa centrado en esa ubicación
mapa = folium.Map(location=pos_actual, zoom_start=13)

# Ponemos un marcador en esa ubicación
folium.Marker(
    location=pos_actual, # Marcador en la ub. marcada en los sliders
    tooltip="Aquí estoy",
    icon=folium.Icon(color="red", icon="home")
).add_to(mapa)

# Creamos un circulo alrededor de la zona objetivo
zona_objetivo = (28.1235, -15.4366)
folium.Circle(
    location=zona_objetivo,
    radius=radio_alarma, # Para que coincida con la alarma
    color='blue',
    fill=True,
    fill_opacity=0.2,
    tooltip="Zona objetivo"
).add_to(mapa)

# Mostramos el mapa en Streamlit
st_data = st_folium(mapa, width=700, height=500)

# Calculamos la distancia 
distancia = geodesic(pos_actual, zona_objetivo).meters
st.write(f"Distancia actual: {distancia:.2f}metros")

# Lógica de la alarma
if distancia <= radio_alarma: # Dentro de la zona objetivo
    st.success("¡¡¡¡¡¡DESPIERTA!!!!!!!")
else:
    st.success("Todavía no ha sonado la alarma, descansa...")