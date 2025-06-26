import streamlit as st
from streamlit_folium import st_folium
from utils import set_ubicaciones, controles_alarma_sin_ruta, crear_mapa, actualizar_ubicaciones_por_clic

st.title("🔨 Configuración de la alarma")
st.session_state.radio_alarma = st.slider("Radio de la alarma", 100, 1000, 500)

st.session_state.modo, st.session_state.ubicacion_actual, st.session_state.zona_objetivo = set_ubicaciones()

controles_alarma_sin_ruta()
mapa = crear_mapa(st.session_state.ubicacion_actual, st.session_state.zona_objetivo, st.session_state.radio_alarma)
st_data = st_folium(mapa, width=700, height=500)  # Mostramos el mapa en Streamlit

st.session_state.ubicacion_actual, st.session_state.zona_objetivo = actualizar_ubicaciones_por_clic(st_data, st.session_state.modo)