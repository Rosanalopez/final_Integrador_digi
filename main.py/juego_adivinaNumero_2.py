
import random


class NumeroSecreto():

    def __init__(self):
        self.ganar = 0
        self.perder = 0
        self.empatar = 0
        self.partida = 0
        self.nombre = ""

    print("*********************")
    print("Preparado para jugar?")
    print("*********************") 
    print("")

    def jugador(self, nombre):
       self.nombre = nombre
       print(nombre)

    def jugar(self):
       print("")
       print("Te desafio a vencer a la compu!!!")
    while True:
          try:
               jugador_1 = int(input("Ingrese un numero entero de 0 a 5:  "))
               #if jugador_1 >= 6:
                 #print("Recuerde q solamente puede ingresar del 0 al 5")
                 #jugador_1 = int(input("Ingrese un numero entero de 0 a 5:  "))
               computador = random.randint(0, 5)
               print("La maquina seleccionó el numero:", computador)
               print(" ")
                 
               if jugador_1 == computador:
                  print("FELICIDADES HAS GANADO!!!")
                  ganar = ganar + 1
                  partida = partida + 1
                  print("")
               elif jugador_1 != computador:
                  print("HAS PERDIDO!!!")
                  perder = perder + 1
                  partida = partida + 1
                  print("")
          except:
                print("Solo puede ingresar numeros")
                print("")
                continuar = input("Seleccione la tecla S para seguir jugando O cualquier tecla para continuar divirtiendote!! == ").lower()
                print("=========================================================================================================")
                if continuar != "s":
                  break
                  print("")
          def puntaje(self):
            print(f"Se han jugado un total de {self.partida} partidas")
            print("")
            print(f"{self.nombre} has tenido un total de {self.ganar} partida/s ganadas")
            print("")
            print(f"La maquina ha obenido un total de  {self.perder} partida/s ganadas")
            print("")

          def resultado_final(self):
           if self.ganar > self.perder:
            print(f"{self.nombre} eres el ganador final!!")
            print("")
           elif self.perder > self.ganar:
            print(f"La maquina ha sido el ganador final!!\nHasta la proxima revancha!!!")
            print("")
           elif self.ganar == self.perder:
            print(f"Se ha producido un empate")
            print("")     