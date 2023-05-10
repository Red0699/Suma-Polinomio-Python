from tkinter import *
import re

# Crear la ventana
ventana = Tk()
ventana.geometry("600x400")  # ajustar el tamaño de la ventana
ventana.title("Simplificación de polinomios")
ventana.config(bg="#293241")

# Función para simplificar el polinomio
def simplificar():
    from sympy import sympify, simplify

    # Obtener el polinomio ingresado por el usuario
    polinomio = entrada.get()

    # Reemplazar términos sin operador de multiplicación con operador de multiplicación
    polinomio_con_multiplicacion = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", polinomio)

    # Convertir el polinomio a una expresión de Sympy y simplificarlo
    polinomio_simplificado = simplify(sympify(polinomio_con_multiplicacion))

    # Convertir el polinomio simplificado a una cadena con notación de exponente
    polinomio_formateado = str(polinomio_simplificado).replace("**", "^").replace("*", "")

    # Mostrar el resultado en la etiqueta de salida
    salida.config(text="Polinomio simplificado: " + polinomio_formateado)

# Función para validar el contenido de la entrada de texto
def validar_entrada(polinomio):
    # Verificar si la entrada contiene caracteres no permitidos
    if not all(c.isdigit() or c.isalpha() or c in '+-*/^' for c in polinomio):
        salida.config(text="Error: la entrada contiene caracteres no permitidos.")
        return False

    # Si la entrada es válida, borrar el mensaje de error anterior (si lo hay)
    salida.config(text="")
    return True

# Crear la etiqueta de entrada
Label(ventana, text="Ingrese un polinomio:", font=("Arial", 16), fg="#fff", bg="#293241").pack(pady=20)

# Crear la entrada de texto para el polinomio
entrada = Entry(ventana, width=40, font=("Arial", 16), validate="key")
entrada.pack()

# Crear el mensaje de aviso
mensaje = Label(ventana, font=("Arial", 12), fg="red", bg="#293241")
mensaje.pack()

# Crear el botón para simplificar el polinomio
boton = Button(ventana, text="Calcular", command=lambda: validar_entrada(entrada.get()) and simplificar(),
                font=("Arial", 14), bg="#FFC857", fg="#000", bd=0, padx=20, pady=10)
boton.pack(pady=20)

# Crear la etiqueta de salida
salida = Label(ventana, font=("Arial", 12), fg="#fff", bg="#293241")
salida.pack()

# Ejecutar la ventana
ventana.mainloop()
