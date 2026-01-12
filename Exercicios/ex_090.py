'''
Crie uma classe chamada Livro que tenha
dois atributos: titulo e autor.
Instancie três objeto dessa classe e
imprima os valores dos atributos.
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        print(self.titulo, self.autor) # nao fazer assim


livro1 = Livro('FansFans','Ricardo Mourão')
livro2 = Livro('asdwadsadwada', 'Pedro')
livro3 = Livro('Norwegian Wood', 'Haruki Murakami')
