def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b


def calculadora():
    print("Calculadora en Python")
    print("Operaciones: sumar, restar, multiplicar, dividir")
    op = input("Selecciona operación: ").lower()

    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
    except ValueError:
        print("Error: entrada no válida")
        return

    if op == "sumar":
        print(f"Resultado: {sumar(a, b)}")
    elif op == "restar":
        print(f"Resultado: {restar(a, b)}")
    elif op == "multiplicar":
        print(f"Resultado: {multiplicar(a, b)}")
    elif op == "dividir":
        print(f"Resultado: {dividir(a, b)}")
    else:
        print("Operación no válida")


if __name__ == "__main__":
    calculadora()