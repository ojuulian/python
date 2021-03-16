# Generando la clase lápiz

class Lapiz:
    color = 'Amarillo'
    contiene_borrador = False
    usa_grafito = True
                                #metodos (todas las funciones valen para metodos)
    def dibujar(self):
        print("El lápiz está dibujando")

    def borrar(self):                  #Llamando un metodo dentro de otro metodo con self
        if self.es_valido_para_borrar():
            print("El lápiz esta dibujando")
        else:
            print("No es posible borrar")

        print("El lápiz está borrando")

    def es_valido_para_borrar(self):   #en un método puede mandar a ejecuttar otro método
        return self.contiene_borrador  #me va a arrojar verdadero o falso


lapiz_generico = Lapiz()        #esto es un objeto
lapiz_generico.dibujar()
lapiz_generico.borrar()
lapiz_generico.contiene_borrador  = True  #Por ser atributo se puede cambiar valores a atributos
print(lapiz_generico.color)
print(lapiz_generico.usa_grafito)

#supeditando cuando borrar pueda usarse solamente si el lapiz tiene borrador