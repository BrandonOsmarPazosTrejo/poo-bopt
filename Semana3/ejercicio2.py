class Convertidor_de_termperatura():
    '''
    Nombre:Brandon Osmar Pazos Trejo
    Grupo: tics 21
    Gecha: 14/02/2021
    Descripcion: primero en lista=[] se pondran los tres grados, en forma de lista despues poner que seran 3 entradas, de las cuales se sumaran los grados se divira entre cuantos son las temperaturas ingrsadas despues usas la formula para convertir a °Farenheit
    '''

    def x (self):
        self.entrada = int(input("Número de temperaturas: "))
        lista = []
        b = 0
        for a in range(self.entrada):
            C = int(input("Temperatura {} en Celsius: ".format(a + 1)))
            lista.append(C)
            b += C
        y = (b/self.entrada) * 1.8 + 32
        print(" Resultado {}°Farenheit".format(y))


objeto = Convertidor_de_termperatura()
objeto.x()