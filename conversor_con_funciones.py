# def imprimir_mensaje():
#     print("Mensaje especial")
#     print("esta línea se volvio a imprimir")

# imprimir_mensaje() 
# imprimir_mensaje() 
# imprimir_mensaje() 
# imprimir_mensaje() 
# imprimir_mensaje() 

def conversacion(mensaje):
    print("Hola")
    print("Cómo estás")
    print(mensaje)
    print("Adios")

opcion = int(input("Selecciona una opcion (1,2,3) "))
if opcion ==1:
    conversacion("Seleccionaste la opción 1  ")
elif opcion ==2:
    conversacion("Seleccionaste la opción 2  ")
elif opcion ==3:
    conversacion("Seleccionaste la opción 3  ")
else:
    print("Escribe una opción valida: ")