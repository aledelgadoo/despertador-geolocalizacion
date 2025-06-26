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


if __name__ == "__main__":
    main()
