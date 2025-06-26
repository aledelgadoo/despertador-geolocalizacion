import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic
from utils import avanzar_ruta, crear_ruta_simulada, crear_mapa, logica_alarma, set_ubicaciones, actualizar_ubicaciones_por_clic, controles_alarma_sin_ruta, calcular_distancia, reproducir_sonido


def main():
    '''
    Genera los títulos de la página web, inicializa las variables necesarias para que funcione
    la página (radio_alarma, zona_objetivo, ruta), y llama a todas el resto de las funciones
    '''

    # Titulos y texto que se mostrará en la página web
    st.title("⏰ Despertador por geolocalización")
    st.write("By Alejandro D.")

    radio_alarma = st.slider("Radio de la alarma", 100, 1000, 500)

    modo, ubicacion_actual, zona_objetivo = set_ubicaciones()

    controles_alarma_sin_ruta()

    # Inicializamos paso
    if "paso" not in st.session_state:
        st.session_state.paso = 0

    # Creamos ruta simulada entre ubicacion_actual y zona_objetivo
    ruta = crear_ruta_simulada(ubicacion_actual, zona_objetivo, pasos=20)

    avanzar_ruta(ruta)

    mapa = crear_mapa(ubicacion_actual, zona_objetivo, radio_alarma, ruta)
    st_data = st_folium(mapa, width=700, height=500)  # Mostramos el mapa en Streamlit

    ubicacion_actual, zona_objetivo = actualizar_ubicaciones_por_clic(st_data, modo)

    # Recuperar siempre los valores del session_state
    ubicacion_actual = st.session_state.ubicacion_actual
    zona_objetivo = st.session_state.zona_objetivo

    
    distancia = calcular_distancia(ubicacion_actual, zona_objetivo)
    logica_alarma(distancia, radio_alarma)


if __name__ == "__main__":
    main()
