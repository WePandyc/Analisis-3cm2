def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

try:
    numero = int(input("Ingresa un número para calcular su factorial: "))
    if numero < 0:
        print("El factorial no está definido para números negativos.")
    else:
        resultado = factorial(numero)
        print(f"El factorial de {numero} es {resultado}")
except ValueError:
    print("Por favor, ingresa un número entero válido.")
