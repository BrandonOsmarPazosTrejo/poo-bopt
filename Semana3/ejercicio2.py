class Convertidor_de_termperatura():
  

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