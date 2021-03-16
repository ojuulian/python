# Inicializando los atributos (colocar valores por default) por medio del contructor

class Lapiz:
                                  #metodos (todas las funciones valen para metodos)

    # def __init__(self):
    #     self.color = 'Amarillo'
    #     self.contiene_corrador = False
    #     self.usa_grafito = True

    def __init__(self, color, contiene_borrador , usa_grafito):
        self.color = color
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito


    def dibujar(self):
        print("El lápiz está dibujando.")

    def borrar(self):                  #Llamando un metodo dentro de otro metodo con self
        if self.es_valido_para_borrar():
            print("El lápiz esta borrando.")
        else:
            print("No es posible borrar.")


    def es_valido_para_borrar(self):   #en un método puede mandar a ejecuttar otro método
        return self.contiene_borrador  #me va a arrojar verdadero o falso


lapiz_generico = Lapiz("Verde" , True, True)        #esto es un objeto == es una isntancia
lapiz_generico.dibujar()
lapiz_generico.borrar()


#supeditando cuando borrar pueda usarse solamente si el lapiz tiene borrador