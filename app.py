import streamlit as st
from PIL import Image

st.title("Primer intento")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("babyyoda.jpg")

st.image(image, caption="Baby Yoda")

texto = st.text_input("Baby Yoda, The Mandalorian", "Capítulo 2, Temporada 1")
