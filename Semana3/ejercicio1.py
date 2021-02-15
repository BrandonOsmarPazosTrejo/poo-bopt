class convertidor_de_dias():
    
    #Nombre:Brandon Osmar Pazos Trejo
    #Grupo: tics 21
    #Gecha: 14/02/2021
    #Descripcion: Primero es saber la formula y convertir los dias a segundos primero es saber cuanto equivale  1 dia en segundos.
        
   def formula(self):
       self.cuantos_dias_total = int(input(":"))
       for i in range(self.cuantos_dias_total):
           dias = int(input("{} Pon el dia a convertir: ".format(i+1)))
           convertir = dias*86400
           print("{} Segundos". format(convertir))
objeto = convertidor_de_dias()
objeto.formula()
