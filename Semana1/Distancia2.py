class Lol():
    
      def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)
    def puntos(self, x1, y1, x2, y2):
       
        Distancia= math.sqrt((x2-x1)**2+(y2-y1)**2)
     print=(math.sqrt(Distancia))

objeto=Lol()
objeto.puntos(3.17,4.78,4.99,7.88)