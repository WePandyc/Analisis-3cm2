import time

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2
def division(num1, num2):
    if num2 == 0:
        return "Error: No se puede dividir por cero"
    return num1 / num2

while True:
    print("Selecciona una operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Ingrese el número de la operación deseada: ")


    if opcion not in ["1", "2", "3", "4"]:
        print("Opción no válida. Por favor, elija una opción válida.")
        continue

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    start_time = time.time()

    if opcion == "1":
        resultado = suma(num1, num2)
        operacion = "Suma"
    elif opcion == "2":
        resultado = resta(num1, num2)
        operacion = "Resta"
    elif opcion == "3":
        resultado = multiplicacion(num1, num2)
        operacion = "Multiplicación"
    elif opcion == "4":
        resultado = division(num1, num2)
        operacion = "División"

    end_time = time.time()
    tiempo_transcurrido = end_time - start_time

    print(f"El resultado de la {operacion} es: {resultado}")
    print(f"Tiempo transcurrido: {tiempo_transcurrido} segundos")


    