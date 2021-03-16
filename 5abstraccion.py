

class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):            #generando un método público
        self._llenar_tanque_de_agua(temperatura)        #underscore
        self._anadir_jabon()                            #variables privadas, a las personas no les interesa conocer
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):      #método prvado
        print(f'Llenando el tanque con agua {temperatura}')

    def _anadir_jabon(self):
        print('Anadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')


if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()