'''
Crie uma classe chamada “Círculo” que
possua um atributo privado para
armazenar o raio e métodos getters e
setters para definir o raio, calcular a
área e o perímetro do círculo.
'''
import math

class Circulo:
    def __init__(self):
        self.__raio = 0

    def get_raio(self):
        return self.__raio

    def set_raio(self, n_raio):
        self.__raio = n_raio

    def calc_area(self):
        Pi = math.pi
        raio = self.get_raio()
        area = Pi * (raio*raio)
        return area

    def calc_perimetro(self):
        Pi = math.pi
        raio = self.get_raio()
        perimetro = 2 * Pi * raio
        return perimetro

new = Circulo()

raio_input = int(input('Digite o raio do circulo: '))
new.set_raio(raio_input)

area = new.calc_area()
perimetro = new.calc_perimetro()

print(f'Area = {area:.2f}\nPerimetro = {perimetro:.2f}')