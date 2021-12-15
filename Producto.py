class Producto:

    def __init__(self, codigo,nombre,precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio
    
    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self,valor):
        self.__codigo=valor    

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,valor):
        self.__nombre=valor    

    @property
    def precio(self):
        return self.__precio

    @precio.setter
    def precio(self,valor):
        self.__precio=valor        

    def __str__(self):
        return f'codig: {str(self.__codigo)} nombre: {self.__nombre} precio: {str(self.__precio)}'


    def calcular_total(self,unidades):
        return self.precio*unidades

p1 = Producto(1,'producto 1', 5)
p2 = Producto(2,'producto 2', 10)
p3 = Producto(3,'producto 3', 20)

print(p1)
print(p2)
print(p3)

print(p1.calcular_total(5))
print(p2.calcular_total(5))
print(p3.calcular_total(5))