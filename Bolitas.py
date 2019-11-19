class Bolita:
    def __init__(self,nombre,cantidad):
        self.name = str(nombre);
        self.quantity = int(cantidad);

    def extraer(self):
        self.quantity -= 1

    def printer(self):
        print("Nombre del Color: {}, Cantidad de Bolitas: {}".format(self.name,self.quantity))

    def suma(self,cantidad):
        self.quantity += cantidad