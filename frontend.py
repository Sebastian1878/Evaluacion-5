import streamlit as st
import requests

# Función para calcular la subsecuencia común más larga entre dos cadenas
def lcs(string1, string2):
    url = "http://localhost:5000/lcs"
    data = {"string1": string1, "string2": string2}
    response = requests.get(url, params=data)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        return None

# Función para calcular el n-ésimo término de la secuencia de Fibonacci
def fibonacci(n):
    url = "http://localhost:5000/fibonacci"
    data = {"n": n}
    response = requests.get(url, params=data)
    if response.status_code == 200:
        return response.json()["result"]
    else:
        return None

# Título de la aplicación
st.title("Subsecuencia común más larga & términos de Fibonacci")

# Checkbox para seleccionar la acción a realizar
action = st.selectbox("Seleccione una acción:", ["Calcular subsecuencia común más larga", "Calcular término de Fibonacci"])

if action == "Calcular subsecuencia común más larga":
    # Ingreso de las cadenas
    string1 = st.text_input("Ingrese la primera cadena:")
    string2 = st.text_input("Ingrese la segunda cadena:")

    # Botón para calcular la subsecuencia común más larga
    if st.button("Calcular"):
        if string1 and string2:
            result = lcs(string1, string2)
            if result:
                st.write(f"La subsecuencia común más larga entre '{string1}' y '{string2}' es: {result}")
            else:
                st.write(f"Entre '{string1}' y '{string2}' no hay subsecuencia común más larga.")
        else:
            st.write("Por favor, ingrese ambas cadenas.")
else:
    # Ingreso del término
    n = st.number_input("Inserta un número", value=0, placeholder="5")

    # Botón para calcular el término
    if st.button("Calcular"):
        if n >= 0:
            result = fibonacci(n)

            if result is not None:
                st.write(f"El {n}-ésimo término de la secuencia de Fibonacci es: {result}")
            else:
                st.write("Ocurrió un error al calcular el término de Fibonacci.")
        else:
            st.write("Por favor, ingrese un término mayor a 0")