import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic


def avanzar_ruta(ruta):
    # Botón para avanzar en la ruta
    if st.button("🚶 Avanzar al siguiente punto"):
        if st.session_state.paso < len(ruta) - 1:
            st.session_state.paso += 1
            st.session_state.ubicacion_actual = ruta[st.session_state.paso]


def crear_ruta_simulada(p1, p2, pasos=10):
    '''
    Crea una lista de coordenadas entre p1 y p2.
    '''
    lat1, lon1 = p1
    lat2, lon2 = p2

    ruta = []
    for i in range(pasos + 1):
        lat = lat1 + (lat2 - lat1) * i / pasos
        lon = lon1 + (lon2 - lon1) * i / pasos
        ruta.append((lat, lon))
    return ruta


def set_ubicaciones():
    '''
    Inicializa los valores iniciales para las ubicaciones.
    '''
    # Selección de la ubicación actual o zona objetivo
    modo = st.radio("¿Qué quieres seleccionar?", ["Ubicación actual", "Zona objetivo"])

    st.session_state.setdefault("ubicacion_actual", (28.10, -15.43)) # Valores por defecto
    st.session_state.setdefault("zona_objetivo", (28.1235, -15.4366))
    ubicacion_actual = st.session_state.ubicacion_actual
    zona_objetivo = st.session_state.zona_objetivo

    return modo, ubicacion_actual, zona_objetivo


def actualizar_ubicaciones_por_clic(st_data):
    clic = st_data.get("last_clicked")

    if clic:
        st.session_state["ultima_coord_clicada"] = (clic["lat"], clic["lng"])


    # Recuperar siempre los valores del session_state
    ubicacion_actual = st.session_state.ubicacion_actual
    zona_objetivo = st.session_state.zona_objetivo
    
    return ubicacion_actual, zona_objetivo


def crear_mapa(pos_actual, zona_objetivo, radio_alarma, ruta=None):
    '''
    Crea el mapa con el marcador, la zona objetivo y la ruta.
    Devuelve este propio mapa, sin mostrarlo en la web todavía.
    '''

    # Creamos el mapa
    mapa = folium.Map(location=pos_actual, zoom_start=13)

    # Ponemos un marcador en la ubicación del usuario
    folium.Marker(
        location=pos_actual, # Marcador en la ub. marcada en los sliders
        tooltip="Aquí estoy",
        icon=folium.Icon(color="red", icon="home")
    ).add_to(mapa)

    # Creamos un circulo alrededor de la zona objetivo
    folium.Circle(
        location=zona_objetivo,
        radius=radio_alarma, # Para que coincida con la alarma
        color='blue',
        fill=True,
        fill_opacity=0.2,
        tooltip="Zona objetivo"
    ).add_to(mapa)

    # Unimos las coordenadas para mejor visibilidad
    if ruta:
        folium.PolyLine(ruta, color="green", weight=2.5, opacity=1).add_to(mapa)

    return mapa


def controles_alarma_sin_ruta():
    '''
    Muestra botones para activar o desactivar la alarma
    y el estado actual de la misma.
    '''
    st.session_state.setdefault("alarma_activada", False)

    if st.button("🔘 Activar alarma"):
        st.session_state.alarma_activada = True

    if st.button("🛑 Desactivar alarma"):
        st.session_state.alarma_activada = False

    st.info(f"Estado de la alarma: {'ACTIVADA' if st.session_state.alarma_activada else 'DESACTIVADA'}")



def logica_alarma(distancia, radio_alarma):
    '''
    Muestra el estado actual de la alarma y la distancia desde la ubicación actual hasta la zona objetivo.
    Contiene la lógica de la alarma
    '''
   
    # Mostramos la distancia actual
    st.write(f"Distancia actual: {distancia:.2f} metros")

    # Lógica de la alarma
    if st.session_state.alarma_activada:
        if distancia <= radio_alarma: # Dentro de la zona objetivo
            reproducir_sonido()
            st.success("¡¡¡¡¡¡DESPIERTA!!!!!!!")
        else:
            st.success("Todavía no ha sonado la alarma, descansa...")
    else:
        st.warning("La alarma no está encendida")


def calcular_distancia(p1, p2):
    '''
    Calcula la distancia entre 2 puntos, en metros.
    '''
    return geodesic(p1,p2).meters


def reproducir_sonido():
      st.markdown(
        """
        <audio autoplay>
          <source src="https://actions.google.com/sounds/v1/alarms/alarm_clock.ogg" type="audio/ogg">
        </audio>
        """,
        unsafe_allow_html=True
    )

