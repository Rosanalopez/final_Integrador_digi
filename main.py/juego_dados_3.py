import random

class Dados():

    def __init__(self):
        self.dado_1 = 0
        self.dado_2 = 0
        self.numero_minimo = 1
        self.numero_maximo = 6
        self.partidas = 0
        self.ganar = 0
        self.perder = 0
        self.nombre = ""

    def jugador(self,nombre):
        self.nombre = nombre
        print(nombre)

    
    def jugar(self):
        while True:
            tirar_dados = input("Deseas tirar los dados SI/NO == ").lower()
            print("")
            if tirar_dados == "no" or tirar_dados == "n":
                break
            self.dado_1 = random.randint(self.numero_minimo, self.numero_maximo)
            print(self.dado_1)
            self.dado_2 = random.randint(self.numero_minimo, self.numero_maximo)
            print(self.dado_2)
            self.partidas = self.partidas + 1
            if self.dado_1 == self.dado_2:
                print("Los numeros de ambos dados son iguales.\nFELICIDADES!!!.\nGANASTE!!!")
                self.ganar = self.ganar + 1

            elif self.dado_1 != self.dado_2:
                print("No coincidien los numeros.\nPERDISTE!!")
                self.perder = self.perder + 1
            print("")

    def puntajes(self):
        print(f"Se han judado un total de {self.partidas}")
        print("")
        print(f"{self.nombre} has ganado un total de {self.ganar} partidas!!..")
        print("")
        print(f"{self.nombre} has perdido un total de {self.perder} partidas!!..")
        print("")
    def resultado_final(self):
        if self.ganar > self.perder:
            print(f"Eres el ganador final del juego")
            print("")
        elif self.ganar < self.perder:
            print(f"Has perdido mas veces de las que has ganado. Sigue intentando")
            print("")
        elif self.ganar == self.perder:
            print("Se ha producido un empate, has ganado y perdido las mismmas cantidad de veces.\nAimate a la revancha")
        print("")

if __name__=="__actividad_principal__":
   dado = Dados() 
   dado.print_resulatdo_final()       
