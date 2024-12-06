class Libro:

    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descripcion(self):
        return f"Libro: {self.titulo}; Autor: {self.autor}"

    def __str__(self):
        return f"Libro: {self.titulo}; Autor: {self.autor} STR"

class LibroDigital(Libro):

    def __init__(self, titulo, autor, formato):
        super().__init__(titulo, autor)
        self.formato = formato

    def descripcion(self):
        return f"Libro: {self.titulo}; Autor: {self.autor}; Formato: {self.formato}"

    def __str__(self):
        return f"Libro: {self.titulo}; Autor: {self.autor}; Formato: {self.formato} STR"

libro1 = Libro("El señor de los anillos", "JRR Tolkien")
libroDigital1 = LibroDigital("Habitos Atomicos", "James Clear", "PDF")

print(libro1.titulo)
print(libro1.autor)

print(libro1.descripcion())
print(libro1.__str__())

print(libroDigital1.descripcion())
print(libroDigital1.__str__())