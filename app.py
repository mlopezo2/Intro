import streamlit as st
from PIL import Image

st.title("Primer intento")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("babyyoda.jpg")

st.image(image, caption="Baby Yoda")

texto = st.text_input("Capítulo 2, Temporada 1", "Baby Yoda, The Mandalorian")
st.write("En la primera temporada descubrimos que el nombre real de Baby Yoda es Grogu. Pertenece a la misma especie del icónico maestro Yoda, de quien no se ha podido definiren la mitología del mundo cual es el nombre de su especie o de qué planeta proviene.")
