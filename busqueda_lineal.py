import time

arreglo = [7,50,0,5,9,2]
x = 5
inicio = time.time()
for i in range (0, len (arreglo)):
    if x == arreglo [i]:
        print('El elemento está en la lista, en la posición: ', i)

fin = time.time()
tiempo_final = fin - inicio

print('El riempo tanscurrido fue: ', tiempo_final)