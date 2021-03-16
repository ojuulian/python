# Generando la clase lápiz

class Lapiz:
    color = 'Amarillo'
    contiene_borrador = False
    usa_grafito = True
                                #metodos (todas las funciones valen para metodos)
    def dibujar(self):
        print("El lápiz está dibujando")

    def borrar(self):
        print("El lápiz está borrando")

lapiz_generico = Lapiz()        #esto es un objeto
lapiz_generico.dibujar()
lapiz_generico.borrar()         #Para llamar un metodo hay que colocar parentesis
print(lapiz_generico.color)
print(lapiz_generico.usa_grafito)