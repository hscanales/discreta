from Bolitas import Bolita
import random

class Caja:
    contenedor = []
    bolitas = 0

    def crear(self):
        nombre = str(input("Ingrese nombre del color: ")).upper()
        cantidad = int(input("Ingrese cantidad de bolitas: "))
        bola = Bolita(nombre, cantidad)
        for i in self.contenedor:
            if nombre == i.name:
                print("El color que ingreso ya existe, se han sumado los datos")
                i.suma(cantidad)
                return 0
        self.contenedor.append(bola)

    def total(self):
        self.bolitas = 0
        for i in self.contenedor:
            self.bolitas += i.quantity

    def printer(self):
        for i in self.contenedor:
            i.printer()

    def proba(self):
        self.total()
        cont = 0
        if (self.bolitas == 0):
            print("No existen mas bolitas en la caja")
            return 0
        for i in self.contenedor:
            probabilidad = round((float(i.quantity) / self.bolitas) * 100,2)
            if(probabilidad==0):
                self.contenedor.pop(cont)
            cont+=1
            print("La probabilidad de que salga una bolita color {} es de {}%".format(i.name, probabilidad))

    def sacar(self):
        random.seed(random.random())
        if (self.bolitas == 0):
            print("No existen mas bolitas en la caja")
            return 0
        top = len(self.contenedor)-1
        index = random.randint(0,top)
        self.contenedor[index].extraer()
        print("Se extrajo una bolita de color {}".format(self.contenedor[index].name))
        self.proba()
