import time #librería para el tiempo

inicio = time.time()
res = 0
for i in range(0, 1000):
        res = res + 1
print (res)
print ('hola mundo!')
fin = time.time()
tiempo_ejecutado = fin - inicio
print (tiempo_ejecutado)