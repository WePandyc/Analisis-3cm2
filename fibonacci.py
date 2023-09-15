def fibonacci(n):
    fibo=[0,1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1]+fibo[i-2])
    return fibo[n]
n=10
resultado=fibonacci (n)
print(resultado)