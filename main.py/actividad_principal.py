import juego_piedra_papel_tijera_1
import juego_adivinaNumero_2
import juego_dados_3
import jugando_grafico_4


class ActividadPrincipal():
    def __init__(self):
        self.inicio = 0
    def iniciar(self):
   

     while True:
                try:
                    print("Bienvenido..!!! a Jugar!!..Elija una opcion del 1 al 5")
                    print("****************************************************")
                    print("Estas preparado??..Tu desafio..Ganarle a la compu..")
                    print("****************************************************")
                    print("****************************************************")
                    print("Opción 1 = Jugar a “piedra, papel, tijera” ")
                    print("Opción 2 = Numero Escondido!! A descubrir el numero secreto ")
                    print("Opción 3 = Tirar un dado.")
                    print("Opción 4 = Grafico - Funciones Matematicas - IMC_OMS")
                    print("Opcion 5 = Salir")
                    print("Escriba con numero la acitiviad que desea realizar")
                    print("")
                    actividad = int(input("Ingrese la opcion deseada = "))
                    print("")
                    if actividad == 1:
                        print("Usted eligió la opción 1  Jugar a “piedra, papel, tijera” ")
                        juego = juego_piedra_papel_tijera_1.PiedraPapeloTijera()
                        print("Bienvenido al PIEDRA - PAPEL - TIJERA")
                        nombre = input("Ingrese su nombre = ")
                        juego.jugador(nombre)
                        juego.jugar()
                        juego.resultado()
                        juego.resultado_final()
                        print("")
                    elif actividad == 2:
                        print("Usted eligió la opción 2 Adivinar un número ")
                        juego_numero = juego_adivinaNumero_2.NumeroSecreto()
                        print("Bienvenido al Adivine el numero")
                        nombre = input("Ingrese su nombre = ")
                        juego_numero.jugador(nombre)
                        juego_numero.jugar()
                        juego_numero.resultado()
                        juego_numero.resultado_final()
                        print("")
                    elif actividad == 3:
                        print("Usted eligió la opción 3 Tirar dados.")
                        juego_dado = juego_dados_3.Dados()
                        print("Bienvenido la tira de de dados")
                        nombre = input("Ingrese su nombre = ")
                        juego_dado.jugador(nombre)
                        juego_dado.jugar()
                        juego_dado.puntajes()
                        juego_dado.resultado_final()
                        print("")
                    elif actividad == 4:
                        print("Usted elegió la opcion 4 Graficar una función matemática.")
                        print("IMC segun OMS")
                        print("")
                        registro = jugando_grafico_4.IMC()
                        registro.ingreso()
                        registro.promedios()
                        registro.grafico()
                        print("")

                    elif actividad >= 6:
                        print("Recuerde que las opciones son del 1 al 5")
                        print("Vuelva a ingresar la opción")
                    elif actividad == 5:
                        print("Salir")
                        break

                    inicio = input("Para continuar con juego escriba SI o S, de lo contrario cualquier presione cualquier tecla = ").lower()
                    if inicio == "si" or inicio == "s":
                        print("Se continua con actividad")
                        print("")

                    else:
                        print("No escribio SI ni tampoco la letra S")
                        print("Por lo tanto se da finalizada la actividad")
                        break
                    print("")
                except:
                    print("Solo debe ingresar numeros")
                    print("")


inicio_actividad = input("Comenzamos a JUGAR? presiona SI o la tecla S, de lo contrario presione cualquier tecla y el programa finalizará = ").lower()
print("")
if inicio_actividad == "si" or inicio_actividad == "s":
    comenzar = ActividadPrincipal()
    comenzar.iniciar()
    
else:
    print("Presionaste cualquier tecla .. .\nFINN!! Te espero prontito..!")