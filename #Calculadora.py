# Calculadora
import math


def principio_calculadora():
    print("---------------Calculadora basica---------------")
    print("""
    Las operaciones disponibles son:
         
    1-Sumar
    2-Restar
    3-Dividir
    4-Multiplicar \n""")

    while True:
        operacion = input("Cual deseas realizar: ")

        try:
            operacion = int(operacion)
            if operacion in [1, 2, 3, 4]:
                break
            else: 
                print("Escribe una operacion valida (1-4)")

        except ValueError:
            print("Para seleccionar la operacion elige del 1 al 4")

    while True:
        primer_numero = input("\nPrimer numero: ")
        segundo_numero = input("Segundo numero: ")

        try:
            primer_numero = float(primer_numero)
            segundo_numero = float(segundo_numero)
            break  # Exit the loop if conversion succeeds
        except ValueError:
            print("Insertar un numero valido")

    if operacion == 1:
        print(primer_numero + segundo_numero)
    elif operacion == 2:
        print(primer_numero - segundo_numero)
    elif operacion == 3:
        print(primer_numero / segundo_numero)
    elif operacion == 4:
        print(primer_numero * segundo_numero)

i=0

while True:

    if i == 0:
        principio_calculadora()
        i += 1
    if i >= 1:
        volver_usar = input("\nQuieres volver a usarla de nuevo? (Si/No) ")
        if volver_usar.lower() == "si":
            principio_calculadora()
        else:
            print("\nGracias por usar la calculadora")
            break
