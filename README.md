# ⏰ Despertador por Geolocalización

Una aplicación interactiva desarrollada con **Streamlit** que permite establecer una zona geográfica como objetivo para activar una alarma cuando el usuario se acerque a ella. Ideal para viajeros, estudiantes o quienes necesitan despertarse en función de su ubicación y no de una hora específica.

---

## 🚀 Funcionalidades

- 📍 Selección de ubicación actual y zona objetivo sobre un mapa.
- 📏 Configuración del radio de activación de la alarma.
- 🛣️ Simulación de ruta y movimiento hacia la zona objetivo.
- 🔊 Alarma sonora al entrar en el radio especificado.
- 🧭 Interfaz dividida en páginas: **Configuración** y **Simulación**.
- 🗺️ Visualización dinámica del trayecto con `folium`.

---

## 🧰 Tecnologías utilizadas

- [Python 3.11+](https://www.python.org)
- [Streamlit](https://streamlit.io)
- [folium](https://python-visualization.github.io/folium/)
- [geopy](https://geopy.readthedocs.io/)
- [streamlit-folium](https://github.com/randyzwitch/streamlit-folium)

---
## 🛠️ Instalación
1. Clona el repositorio
```bash
git clone https://github.com/tu-usuario/despertador-geolocalizacion.git
cd despertador-geolocalizacion
```
2. Crea un entorno virtual e instala las dependencias:
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
3. Ejecuta la aplicación
```bash
streamlit run app.py
```
---

## 🎯 Uso
1. Ve a la página Configuración para seleccionar:
- La Ubicación actual
- La Zona objetivo
- El radio de activación

2. Luego, accede a la página Simulación para:
- Avanzar paso a paso en la ruta simulada
- Ver la distancia restante
- Activar la alarma y observar cómo se comporta al entrar en el radio

---

## 📦 Dependencias
```txt
streamlit
folium
geopy
streamlit-folium
```
--- 
## 📝 Licencia
MIT License — libre para usar, modificar y distribuir.
