'''
Adicione um método à classe desenvolvida
no exercício anterior Livro que imprime
uma descrição do livro no formato:

“O livro com o titulo X foi escrito pelo autor Y".
'''

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def print_livros(self):
        print(f'O livro {self.titulo} foi escrito por {self.autor}')

livro1 = Livro('FansFans','Ricardo Mourão')
livro2 = Livro('asdwadsadwada', 'Pedro')
livro3 = Livro('Norwegian Wood', 'Haruki Murakami')

livro1.print_livros()
livro2.print_livros()
livro3.print_livros()