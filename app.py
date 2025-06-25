import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic

# Titulos y texto que se mostrará en la página web
st.title("⏰ Despertador por geolocalización")
st.write("By Alejandro D.")

radio_alarma = 500 # metros

# Simulamos una ruta (una lista de coordenadas)
ruta = [
    (28.1000, -15.4600),
    (28.1050, -15.4500),
    (28.1100, -15.4450),
    (28.1150, -15.4400),
    (28.1200, -15.4370),
    (28.1235, -15.4366),
]
st.session_state.setdefault("paso", 0) # Variable paso por defecto 0

# Posición actual simulada
paso_actual = st.session_state.paso

# Activar/Desactivar alarma
st.session_state.setdefault("alarma_activada", False) # Variable alarma_activada por defecto False

if st.button("🔘 Activar alarma"):
    st.session_state.alarma_activada = True

if st.button("🛑 Desactivar alarma"):
    st.session_state.alarma_activada = False

st.info(f"Estado de la alarma: {st.session_state.alarma_activada}") # Mostramos estado alarma

# Botón para avanzar por la ruta
if st.button("🚶 Avanzar al siguiente punto"):
    if st.session_state.paso < len(ruta) - 1:
        st.session_state.paso += 1
pos_actual = ruta[st.session_state.paso]

# Creamos el mapa centrado en esa ubicación
mapa = folium.Map(location=pos_actual, zoom_start=13)

# Unimos las coordenadas para mejor visibilidad
folium.PolyLine(ruta, color="green", weight=2.5, opacity=1).add_to(mapa)

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
if st.session_state.alarma_activada:
    if distancia <= radio_alarma: # Dentro de la zona objetivo
        st.success("¡¡¡¡¡¡DESPIERTA!!!!!!!")
    else:
        st.success("Todavía no ha sonado la alarma, descansa...")
else:
    st.warning("La alarma no está encendida")