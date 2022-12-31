
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
cmap = mpl.color_sequences['tab10']

# ● Graficar una función matemática.
class IMC():
    def __init__(self):
        self.peso = 0
        self.altura = 0
        self.totalEncuestados = 0
        self.obesidad = 30
        self.normal = 24.99
        self.sobrepeso = 25
        self.bajo_peso = 18.50
        self.imc = 0
        self.encuestadosBajo_peso = 0
        self.encuestadosNormal = 0
        self.encuestadosSobrepeso = 0
        self.encuestadosObesidad = 0
        self.totalEncuestados = 0




    def ingreso(self):
        print("Registro de peso y altura\nComenzar")
        print("")        
        while True:
            try:  
                self.peso = float(input("Peso = "))
                self.altura = float(input("Altura = "))
                self.totalEncuestados = self.totalEncuestados + 1
                self.imc = round (self.peso / (self.altura * self.altura), 2)
                print(" total imc es =",self.imc )
                if self.imc <= self.bajo_peso:
                    self.encuestadosBajo_peso = self.encuestadosBajo_peso + 1
                elif self.imc >= self.obesidad:
                    self.encuestadosObesidad = self.encuestadosObesidad + 1
                elif self.imc <= self.normal and self.imc > self.bajo_peso:
                    self.encuestadosNormal = self.encuestadosNormal + 1
                elif self.imc >= self.sobrepeso and self.imc < self.obesidad:
                    self.encuestadosSobrepeso = self.encuestadosSobrepeso + 1
            except:
                print("Solo puede ingresar numeros")
            print("")
            print("Si desea finalizar presione X, sino presione cualquier letra")    
            continuar = input("Continuar = ").lower()
            if continuar == "x":
                break
            print("")
            
    def promedios(self):
        print("Total")
        print(self.totalEncuestados)
        print("")
        print("Bajo Peso")
        print(self.encuestadosBajo_peso)
        print("")
        print("Normal")
        print(self.encuestadosNormal)
        print("")
        print("sobrepeso")
        print(self.encuestadosSobrepeso)
        print("")
        print("Obesidad")
        print(self.encuestadosObesidad)
        print("")
        
    def grafico(self):
        fig, ax = plt.subplots()
        x= np.array(["Bajo Peso (18.50) ", "Normal(24.99)", 'Sobre Peso(25)', 'Obesidad(30)'])
        y= np.array ([ self.encuestadosBajo_peso, self.encuestadosNormal, self.encuestadosSobrepeso, self.encuestadosObesidad])
        plt.title("IMC_OMS")
        plt.xlabel("IMC")
        plt.ylabel("Cantidad de encuestados")
        bar_labels = (['red', 'blue', 'green', 'orange'])
        bar_colors =(['tab:red', 'tab:blue', 'tab:green', 'tab:orange','tab:red', 'tab:blue', 'tab:red'])
        ax.bar(x, y, label=bar_labels, color=bar_colors)
        ax.set_title(f"IMC Segun la OMS.\nTotal personas encuestadas = {self.totalEncuestados}")
        plt.legend(loc="best")
        #plt.bar(x, y)
        #plt.grid()
        plt.show()