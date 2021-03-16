 
 
# Los siguientes objetos son iterables (se puede utilizar en un bucle definido)
################################## CADENA ##############################
cadena = 'Oscar'
iterador_cadena = iter(cadena)
next(iterador_cadena)
next(iterador_cadena)


################################## LISTAS ##############################
lista = ['a', 'b', 'c']
iterador_lista = iter(lista)
next(iterador_lista)
next(iterador_lista)


################################## TUPLA ###############################
tupla = ('d', 'e', 'f')
iterador_tupla= iter(tupla)
next(iterador_tupla)
next(iterador_tupla)


################################# CONJUNTO #############################
conjunto = {'g', 'h', 'i'}
iterador_conjunto = iter(conjunto)
next(iterador_conjunto)
next(iterador_conjunto)


############################## DICCIONARIO #############################
diccionario = {'rodriguez': 1, 'yepez': 2, 'zambrano': 3}
iterador_diccionario = iter(diccionario)
next(iterador_diccionario)
next(iterador_diccionario)


############################## BUCLE FOR ################################
# Luego pueden construirsen los bucles
frutas = ['manzana', 'pera', 'mango']
for fruta in frutas:
        print(fruta)


print("Usando For loop".center(25,'-'))
for fruta in frutas:
    print(f"\t-{fruta}")


#--
contador = 0

while contador <= 10:
    print(contador, end=' ')
    contador += 1

print('\n\n')


estudaintes = {
    'mexico': 10,
    'colombia': 15,
    'puerto rico': 4
}

print("Estudiantes".center(15, '-'))
for pais in estudaintes:
    print(pais.title())

print('\n')


print("pais".title().rjust(11), "estudiantes".title().rjust(13))
for pais, numero_de_estudiantes in estudaintes.items():
    print(f"{pais.title().rjust(11)} : {numero_de_estudiantes}")
