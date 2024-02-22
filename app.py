import streamlit as st
from PIL import Image

st.title("Primer intento")
st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open("babyyoda.jpg")

st.image(image, caption="Baby Yoda")

texto = st.text_input("Capítulo 2, Temporada 1", "Baby Yoda, The Mandalorian")
st.write("En la primera temporada descubrimos que el nombre real de Baby Yoda es Grogu."
"Pertenece a la misma especie del icónico maestro Yoda, de quien no se ha podido definiren la mitología del mundo cual es el nombre de su especie o de qué planeta proviene.")

st.subheader("Ahora usemos dos columnas.")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Cuestionario")
  st.write("¿Cuál es el nombre real de Baby Yoda?")
  resp = st.checkbox("Grogu")
  if resp:
    st.write("Correcto! Baby Yoda es el nombre dado por el internet por su parecido con el maestro Yoda")


with col2:
  st.subheader("Guía")
  modo = st.radio("¿Qué modalidad es la principal en tu interfaz?", ("Visual", "Auditiva", "Táctil"))
  if modo == "Visual":
    st.write("La vista es fundamental para tu interfaz")
  if modo == "Auditiva":
    st.write("La audición es fundamental para tu interfaz")

st.subheader("Uso de Botones")
if st.button("Presiona el Botón"):
  st.write("Gracias por presionar")
else:
  st.write("No has presionado aún")

st.subheader("Selectbox")
in_mod = st.selectbox(
  "Selecciona la modalidad",
  ("Audio", "Visual", "Háptico"),
  
