# Manejando excepciones en python 


# def divide_elementos_en_lista(lista,divisor):
#     return[i/divisor for i in lista]

# lista = list(range(10))
# divisor = 0
# print(divide_elementos_en_lista(lista,divisor))


def divide_elementos_en_lista(lista,divisor):
    try:
        return[i/divisor for i in lista]
    except ZeroDivisionError as e:
        return lista

lista = list(range(10))
divisor = 0
print(divide_elementos_en_lista(lista,divisor))

