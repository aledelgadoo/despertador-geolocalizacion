import streamlit as st
import folium
from streamlit_folium import st_folium
from geopy.distance import geodesic
from utils import *


def main():
    '''
    Genera los títulos de la página web.
    '''

    # Titulos y texto que se mostrará en la página web
    st.title("⏰ Despertador por geolocalización")
    st.write("By Alejandro D.")
    st.info("Usa el menú de la izquierda para navegar entre páginas 🤝")
    st.write("""
             ¿Cansado de despertarte siempre a la misma hora sin importar dónde estés? ¡Esta app cambia las reglas del juego!

            Con el Despertador por Geolocalización que he diseñado, podrás configurar una zona objetivo geográfica y un radio de alerta. Cuando te acerques a ese lugar, la alarma se activará automáticamente, ayudándote a despertarte justo en el momento y lugar indicados, sin depender del horario fijo.

            Ideal para viajeros, estudiantes o cualquier persona que necesite despertarse según su ubicación actual, no la hora del reloj. Además, la interfaz intuitiva y el mapa interactivo te permiten seleccionar fácilmente tu punto de partida y destino, simulando el recorrido para una experiencia personalizada y precisa.

            ¡Despierta a tiempo, donde sea que estés!

            """)

if __name__ == "__main__":
    main()
