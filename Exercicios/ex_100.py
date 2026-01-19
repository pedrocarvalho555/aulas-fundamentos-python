'''
Desenvolva uma classe Temperatura que
armazene a temperatura em graus Celsius como
um atributo privado. Implemente um getter e
um setter usando property para permitir que a
temperatura seja ajustada e lida em Celsius,
e adicione métodos para converter a
temperatura para Fahrenheit e Kelvin.
'''

class Temperatura():
    def __init__(self, temperatura):
        self.__celsius = temperatura
        self.__kelvin = self.__converte_kelvin()
        self.__fahrenheit = self.__converte_fahrenheit()

    @property
    def temperatura(self):
        return self.__celsius

    @temperatura.setter
    def temperatura(self, temp):
        self.__celsius = temp
        self.__fahrenheit = self.__converte_fahrenheit()
        self.__kelvin = self.__converte_kelvin()

    @property
    def kelvin(self):
        return self.__kelvin

    @property
    def fahrenheit(self):
        return self.__converte_fahrenheit()

    def __converte_fahrenheit(self):
        return self.__celsius + 273.15

    def __converte_kelvin(self):
        return (self.__celsius * 9 / 5) + 32

    def mostrar(self):
        print(f'Fº = {self.__fahrenheit}\nKº = {self.__kelvin}\nCº = {self.__celsius}')

new = Temperatura(30)
print(new.mostrar())
