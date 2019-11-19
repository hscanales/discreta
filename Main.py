from Caja import Caja

caja = Caja()

def continuar():
    while (True):
        flag = str(input("¿Desea continuar ingresando bolitas? Ingrese {} o {} : ".format('"Si"', '"no"'))).upper()
        print("\n\n\n\n")
        if (flag == "NO"):
            return False
        elif (flag == "SI"):
            return True
        else:
            print("Ingrese correctamente la palabra Si o No")

def extraccion():
    caja.sacar()

def main():
    flag = True

    while (flag):
        caja.crear()
        flag = continuar()
    caja.total()
    caja.printer()

    flag=True
    while(flag):
        print("==Menu==\n 1- Mostrar Probabilidades \n 2- Extraer Bolita \n 3- Salir del programa")
        a = int(input("Ingrese su opcion del menu: "))
        if(a==1):
            caja.proba()
            print("\n")
        elif(a==2):
            caja.sacar()
            print("\n")
        elif(a==3):
            flag=False
        else:
            print("Ingreso una opcion no valida intente denuevo")
            print("\n")





if __name__ == "__main__":
    print(
        "Instrucciones de uso: \n 1- Ingrese el nombre del color \n 2- Ingrese la cantidad de bolitas a ingresar: \n ")
    main()

