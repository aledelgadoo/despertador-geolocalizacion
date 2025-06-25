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

    radio_alarma = st.slider("Radio de la alarma", 100, 1000, 500)

    # Selección de la ubicación actual o zona objetivo
    modo = st.radio("¿Qué quieres seleccionar?", ["Ubicación actual", "Zona objetivo"])

    st.session_state.setdefault("ubicacion_actual", (28.10, -15.43)) # Valores por defecto
    st.session_state.setdefault("zona_objetivo", (28.1235, -15.4366))
    ubicacion_actual = st.session_state.ubicacion_actual
    zona_objetivo = st.session_state.zona_objetivo

    controles_alarma_sin_ruta()

    mapa = crear_mapa(ubicacion_actual, zona_objetivo, radio_alarma)
    st_data = st_folium(mapa, width=700, height=500)  # Mostramos el mapa en Streamlit

   # Detectar si se hizo clic y guardar en el session_state
    clic = st_data.get("last_clicked")

    if clic and (clic["lat"], clic["lng"]) != st.session_state.get("last_click_coord"):
        coord = (clic["lat"], clic["lng"])
        st.session_state["last_click_coord"] = coord  # Guarda la última coordenada clicada

        if modo == "Ubicación actual":
            st.session_state.ubicacion_actual = coord
        else:
            st.session_state.zona_objetivo = coord

    # Recuperar siempre los valores del session_state
    ubicacion_actual = st.session_state.ubicacion_actual
    zona_objetivo = st.session_state.zona_objetivo


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