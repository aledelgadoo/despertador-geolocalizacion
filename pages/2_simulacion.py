import streamlit as st
from streamlit_folium import st_folium
from utils import crear_ruta_simulada, avanzar_ruta, crear_mapa, calcular_distancia, logica_alarma

st.title("🏃‍♂️ Simulación de la alarma")
# Inicializamos paso
if "paso" not in st.session_state:
    st.session_state.paso = 0

# Creamos ruta simulada entre ubicacion_actual y zona_objetivo
ruta = crear_ruta_simulada(st.session_state.ubicacion_actual, st.session_state.zona_objetivo, pasos=20)

avanzar_ruta(ruta)

mapa = crear_mapa(st.session_state.ubicacion_actual, st.session_state.zona_objetivo, st.session_state.radio_alarma, ruta)
st_data = st_folium(mapa, width=700, height=500)  # Mostramos el mapa en Streamlit

# Recuperar siempre los valores del session_state
ubicacion_actual = st.session_state.ubicacion_actual
zona_objetivo = st.session_state.zona_objetivo


distancia = calcular_distancia(ubicacion_actual, zona_objetivo)
logica_alarma(distancia, st.session_state.radio_alarma)