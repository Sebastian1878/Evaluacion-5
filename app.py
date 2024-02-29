from flask import Flask, jsonify, request

app = Flask(__name__)

# Diccionario para almacenar los valores calculados previamente
lcs_memo = {}
fib_memo = {0: 0, 1: 1}


def longest_common_subsequence(a, b):
    # Crear una matriz para almacenar la longitud de la subsecuencia común
    lcs = [[[] for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]

    # Llenar la matriz lcs utilizando programación dinámica
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            if b[i - 1] == a[j - 1]:
                # Si los caracteres coinciden, extiende la subsecuencia común anterior
                lcs[i][j] = lcs[i - 1][j - 1] + [b[i - 1]]
            else:
                # Si los caracteres no coinciden, elijes la subsecuencia más larga entre las anteriores
                lcs[i][j] = lcs[i - 1][j] if len(lcs[i - 1][j]) > len(lcs[i][j - 1]) else lcs[i][j - 1]

    # El resultado se encuentra en lcs[len(b)][len(a)]
    return "".join(lcs[len(b)][len(a)])


def fibonacci(n):
    # Calculo de n términos de fibonacci utilizando programación dinámica.
    if n not in fib_memo:
        fib_memo[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return fib_memo[n]


@app.route("/lcs", methods=["GET"])
def lcs_api():
    # Endpoint para calcular la subsecuencia común más larga entre dos cadenas.
    string1 = request.args.get("string1")
    string2 = request.args.get("string2")
    if not string1 or not string2:
        return jsonify({"error": "Ambas cadenas de caracteres son requeridas"}), 400
    if not isinstance(string1, str) or not isinstance(string2, str):
        return jsonify({"error": "Introduce una cadena de texto"}), 400
    result = longest_common_subsequence(string1, string2)
    return jsonify({"result": result})


@app.route("/fibonacci", methods=["GET"])
def fibonacci_api():
    # Endpoint para calcular el n-ésimo término en la secuencia de fibonacci.
    n = int(request.args.get("n"))
    if n < 0:
        return jsonify({"error": "No puede ser un número negativo"}), 400
    result = fibonacci(n)
    return jsonify({"result": result}), 200


if __name__ == "__main__":
    app.run(debug=True)