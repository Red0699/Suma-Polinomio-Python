import re
from sympy import sympify, simplify

# Pedir al usuario que ingrese un polinomio
polinomio = input("Ingrese un polinomio: ")

# Validar que solo se ingresen letras, números y los signos +,-,^,x,y,z
if not re.match(r"^[a-zA-Z0-9\+\-\^\*]*$", polinomio):
    print("El polinomio contiene caracteres inválidos.")
else:
    # Reemplazar términos sin operador de multiplicación con operador de multiplicación
    polinomio_con_multiplicacion = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", polinomio)
    polinomio_con_multiplicacion = re.sub(r"([a-zA-Z])([a-zA-Z])", r"\1*\2", polinomio_con_multiplicacion)

    # Convertir el polinomio a una expresión de Sympy y simplificarlo
    polinomio_simplificado = simplify(sympify(polinomio_con_multiplicacion))

    # Convertir el polinomio simplificado a una cadena con notación de exponente
    polinomio_formateado = str(polinomio_simplificado).replace("**", "^").replace("*", "")

    # Imprimir el polinomio simplificado con notación de exponente
    print("Polinomio simplificado:", polinomio_formateado)
