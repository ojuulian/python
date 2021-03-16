


import time    #para medir el tiempo

def factorial(n): #implementacion iterativa del factorial
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta


def factorial_r(n):  #implementacion recursiva de factorial
    if n == 1:
        return 1

    return n * factorial(n - 1)


if __name__ == '__main__':
    n = 50000
    #n = 200000                    

    comienzo = time.time()      #ejecutando modulo time
    factorial(n)
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    factorial_r(n)
    final = time.time()
    print(final - comienzo)