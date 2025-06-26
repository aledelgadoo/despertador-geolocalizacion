import streamlit as st
from streamlit_folium import st_folium
from utils import set_ubicaciones, controles_alarma_sin_ruta, crear_mapa, actualizar_ubicaciones_por_clic

st.title("🔨 Configuración de la alarma")
st.session_state.radio_alarma = st.slider("Radio de la alarma", 100, 1000, 500)

st.session_state.modo, st.session_state.ubicacion_actual, st.session_state.zona_objetivo = set_ubicaciones()

controles_alarma_sin_ruta()

st.write("Haz click en el mapa para fijar la coordenada de la ubicación que quiera modificar!")

# Mostrar la coordenada seleccionada
if "ultima_coord_clicada" in st.session_state:
    st.info(f"Coordenada seleccionada: {st.session_state['ultima_coord_clicada']}")

    # Botón para confirmar selección
    if st.button("✅ Confirmar ubicación seleccionada"):
        if st.session_state.modo == "Ubicación actual":
            st.session_state.ubicacion_actual = st.session_state["ultima_coord_clicada"]
        else:
            st.session_state.zona_objetivo = st.session_state["ultima_coord_clicada"]


mapa = crear_mapa(st.session_state.ubicacion_actual, st.session_state.zona_objetivo, st.session_state.radio_alarma)
st_data = st_folium(mapa, width=700, height=500)  # Mostramos el mapa en Streamlit


actualizar_ubicaciones_por_clic(st_data)