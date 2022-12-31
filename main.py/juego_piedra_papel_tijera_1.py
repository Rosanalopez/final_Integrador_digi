import random
# ● Jugar a “piedra, papel, tijera” compitiendo contra la computadora.
class PiedraPapeloTijera():
    def __init__(self):
        self.partidas = 0
        self.perder = 0
        self.ganar = 0
        self.empatar = 0
        self.nombre = ""

        
    def jugador(self, nombre):
        self.nombre = nombre
        print(f"{nombre} vs Maquina")

    def jugar(self):
        print("")
        while True:
            
            jugador_1 = input("Escriba la opción deseada\nOpción 1= Piedra \nOpción 2= Papel \nOpción 3= Tijera\nSeleccione la opción = ").lower()

            maquina = random.choice(["piedra", "papel", "tijera"])
            self.partidas = self.partidas + 1

            #Primera parte =  opción papel
            if jugador_1 == "papel" and maquina == "papel":
                print(f"Empate!!!\nAmbos jugadores elegieron Papel")
                self.empatar = self.empatar + 1
                print("")
            elif jugador_1 == "papel" and maquina == "tijera":
                print(f"{self.nombre} eligió papel y la maquina eligió tijera.\nGanador Maquina")
                self.perder = self.perder + 1
                print("")
            elif jugador_1 == "papel" and maquina == "piedra":
                print(f"{self.nombre} papel y la maquina eligió piedra.\nGanador {self.nombre}")
                self.ganar = self.ganar + 1
                print("")

            # Segunda parte =  opción piedra
            elif jugador_1 == "piedra" and maquina == "papel":
                print(f"{self.nombre} eligio piedra y la maquina eligio papel.\nGanador = Maquina")
                self.perder = self.perder + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "tijera":
                print(f"{self.nombre} eligió piedra y la maquina eligió tijera.\nGanador {self.nombre}")
                self.ganar = self.ganar + 1
                print("")
            elif jugador_1 == "piedra" and maquina == "piedra":
                print(f"Empate!!!\nAmbos jugadores elegieron Piedra")
                self.empate = self.empate + 1

            # Tercera parte = opción tijera
            elif jugador_1 == "tijera" and maquina == "tijera":
                print(f"Empate!!!\nAmbos jugadores elegieron Tijera")
                self.empatar = self.empatar + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "papel":
                print(f"{self.nombre} eligió tijera y la maquina eligió papel.\nGanador {self.nombre}")
                self.ganar = self.ganar + 1
                print("")
            elif jugador_1 == "tijera" and maquina == "piedra":
                print(f"{self.nombre} eligió papel y la maquina eligió piedra.\nGanador Maquina")
                self.perder = self.perder + 1
                print("")
                
            # continuar o finalizar

            continuar = input("Seleccione la tecla S para seguir jugando sino cualquier tecla == ").lower()
            if continuar != "s":
                break
            print("")

    def resultado(self):
        print(f"Se han jugado un total de {self.partidas} partidas")
        print("")
        print(f"{self.nombre} has tenido un total de {self.ganar} partida/s ganadas")
        print("")
        print(f"La maquina ha obenido un total de  {self.perder} partida/s ganadas")
        print("")
        print(f"Hubo un total de {self.empatar} partida/s que terminaron en empates")
        print("")

    def resultado_final(self):
        if self.ganar > self.perder and self.ganar > self.empatar:
            print(f"{self.nombre} HAS GANADOOOOO!!\nFFELICIDADES!!")
            print("")
        elif self.perder > self.ganar and self.perder > self.empatar:
            print(f"La maquina ha sido la GANADORAA!!")
            print("")
        elif self.empatar > self.perder and self.empatar > self.ganar:
            print(f"HAN EMPATADO!!!.")
            print("")
        elif self.ganar == 0 and self.perder == 0 and self.empatar == 0:
            print("No se ha jugado ninguna partida")
            print("")        
        elif self.ganar == self.empatar and self.perder == self.empatar:
            print("Felicitaciones, has sido el ganado por definición")
            print("")

