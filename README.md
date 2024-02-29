# Evaluacion-5
Subsecuencia común más larga &amp; términos de Fibonacci

# APIs para la Subsecuencia Común Más Larga con Python y Término de Fibonacci
Esta README proporciona detalles sobre el uso del backend (API) y del frontend. La aplicación permite calcular la subsecuencia común más larga entre dos cadenas y obtener el n-ésimo término de la suseción de fibonacci.

## Backend (API) FLASK
El backend es una API que calcula la subsecuencia común más larga entre dos cadenas y el n término de la suseción de fibonacci utilizando programación dinámica y proporciona el resultado a través de solicitudes HTTP.

### Uso Básico
1. Inicia el servidor Flask (asegúrate de tener instalado Flask ejecutando pip install Flask) ejecutando el archivo app.py. Por defecto, se ejecuta en el puerto 5000.
2. Una vez iniciado el servidor, puedes realizar una petición GET a través de curl en la terminal a la ruta /lcs para obtener la subsecuencia común más larga. Por ejemplo: _curl http://localhost:5000/lcs?string1=abc&string2=def_
en el caso de obtener el n término de la suseción de fibonacci puedes realizar una petición GET a través de curl en la terminal a la ruta **/fibonacci** por ejemplo: *curl http://localhost:5000/fibonacci?n=4*
3. La API calculará la subsecuencia común más larga entre las dos cadenas proporcionadas o en el otro caso el n-ésimo término de fibonacci.
4. Se utiliza una matriz para almacenar la longitud de la subsecuencia común entre las dos cadenas y en el caso de fibonacci, se utiliza un diccionario para almacenar los valores obtenidos previamente hasta obtener el deseado (variable fib_memo).
5. En las funciones **longest_common_subsequence** y **fibonacci** es donde se lleva a cabo los cálculos correspondientes.

### Consideraciones a tener en cuenta
- Si no se proporcionan ambas cadenas como parámetros, se devolverá un error con el estatus 400 y el mensaje "Ambas cadenas de caracteres son requeridas".
- Si alguna de las cadenas proporcionadas no es de tipo str, se devolverá un error con el estatus 400 y el mensaje "Introduce una cadena de texto".
- Si se recibe como parámetro un numero negativo, el estatus devuelto será 400 dando como _"error": "No puede ser un número negativo"_
- No cambiar la inicialización del diccionario de memoización de terminos de fibonacci obtenidos 

## Frontend (Streamlit)
Streamlit es un framework para la creación de aplicaciones web orientadas a datos basado en Python, ideal para obtener un diseño sencillo y atractivo.

### Uso Básico
1. Instala Streamlit ejecutando pip install streamlit.
2. Ejecuta el siguiente comando para iniciar el frontend: streamlit run frontend.py.
3. Navega a la URL de localhost establecida.
4. Prueba la aplicación introduciendo las dos cadenas para calcular la subsecuencia común más larga o en el otro caso introduciendo el n término deseado de la suseción de fibonacci.

## Evitar Errores al Modificar el Código

Para evitar errores al modificar el código, sigue estas recomendaciones:

- Antes de realizar cambios, asegúrate de entender completamente cómo funciona cada parte del código.
- Realiza cambios incrementales y prueba después de cada modificación para detectar posibles problemas.
- Mantén un registro de los cambios realizados y prueba de manera exhaustiva para asegurarte de que todas las funcionalidades sigan funcionando correctamente.
- Utiliza control de versiones (por ejemplo, Git) para gestionar los cambios y revertirlos si es necesario.
