
#BÚSQUEDA BINARIA (Crear un algoritmo que encuentre la raiz de un número)


objetivo = int(input("Escribe un número: "))
epsilon = 0.01
inicio = 0
final = max(1, objetivo)
respuesta = 0


while abs(respuesta**2 - objetivo) > epsilon:
    print() 