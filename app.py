import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic


def main():
    '''
    Genera los títulos de la página web, inicializa las variables necesarias para que funcione
    la página (radio_alarma, zona_objetivo, ruta), y llama a todas el resto de las funciones
    '''

    # Titulos y texto que se mostrará en la página web
    st.title("⏰ Despertador por geolocalización")
    st.write("By Alejandro D.")

    radio_alarma = st.slider("Radio de la alarma", 200, 1000, 1)

    # Permitimos al usuario seleccionar la ub. actual y la zona objetivo
    st.subheader("📍 Introduce tu ubicación actual")
    lat_actual = st.number_input("Latitud actual", value=28.10, format="%.6f")  # value == valor por defecto
    lon_actual = st.number_input("Longitud actual", value=-15.43, format="%.6f")
    ubicacion_actual = (lat_actual, lon_actual)

    st.subheader("🎯 Introduce la zona objetivo")
    lat_objetivo = st.number_input("Latitud objetivo", value=28.1235, format="%.6f")
    lon_objetivo = st.number_input("Longitud objetivo", value=-15.4366, format="%.6f")
    zona_objetivo = (lat_objetivo, lon_objetivo)
    
    controles_alarma_sin_ruta()

    mapa = crear_mapa(ubicacion_actual, zona_objetivo, radio_alarma)
    st_data = st_folium(mapa, width=700, height=500)  # Mostramos el mapa en Streamlit

    distancia = calcular_distancia(ubicacion_actual, zona_objetivo)
    logica_alarma(distancia, radio_alarma)


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


def controles_alarma(ruta):
    '''
    Permite activar/desactivar la alarma, muestra el estado actual. 
    Contiene también el botón para avanzar por la ruta.
    '''
    # Valores default de los session_state
    st.session_state.setdefault("paso", 0)
    st.session_state.setdefault("alarma_activada", False)

    if st.button("🔘 Activar alarma"):
        st.session_state.alarma_activada = True

    if st.button("🛑 Desactivar alarma"):
        st.session_state.alarma_activada = False

    # Mostramos estado actual de la alarma
    st.info(f"Estado de la alarma: {st.session_state.alarma_activada}")

    # Botón para avanzar por la ruta
    avanzar = False
    if st.button("🚶 Avanzar al siguiente punto"):
        if st.session_state.paso < len(ruta) - 1:
            st.session_state.paso += 1
            avanzar = True
    
    return avanzar


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

    st.info(f"Estado de la alarma: {st.session_state.alarma_activada}")


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


if __name__ == "__main__":
    main()