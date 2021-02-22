class Tabla_de_evaluacion():
    #Nombre:Brandon Osmar Pazos Trejo
    #Grupo: tics 21
    #Gecha: 14/02/2021
    #Descripcion: while true es para evaluar si lo que esta dentro de el, cumple cada uno con las funciones y poner un segundo bucle, dentro del segundo while se pondra las operaciones y el resultado, dentro del bucle if para comprobar si la condición se cumple y break para cerrar un bucle o ciclo. 
    def __init__(self):
        pass
    def Datos(self):
        while True:
            print("Taba de Evaluación")
            Materia = input("Materia: ")
            Numero_Alumnos = int(input("Número de alumnos: "))
            Nombre_Alumno = input("Nombre alumno: ")
            Clases = int(input("Número de clases: "))
            Faltas = int(input("Número de faltas: "))
            Retardos = int(input("Número de retrasos: "))
            
                
            while Retardos >= 3:
                Faltas += 1
                Retardos -= 3
            x = Faltas * 100 / 10
            porcentaje = 100 - x
            print("Porcentaje de asistencias: {}".format(porcentaje))
            
            if porcentaje <= 80:
                print("Resultado:  No tiene derecho")
                print("")
            else:
                print("Resultado:  Tiene derecho")
                print("")

            repetir = input("Otra evaluación (s/n) ")
            print ("")
            if repetir != "s":
                print("FIN DEL PROGRAMA")
                break
            
                



objeto = Tabla_de_evaluacion()
objeto.Datos()