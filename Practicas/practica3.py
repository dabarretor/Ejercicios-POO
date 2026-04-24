class Publicacion:
    def __init__(self, fecha: str, autor: str, titulo: str):
        self.autor = autor
        self.titulo = titulo
        self.fecha = fecha

    def __str__(self) -> str:
        return f"{self.autor} - {self.titulo}"

class Libro(Publicacion):
    def __init__(self, fecha: str, autor: str, titulo: str, paginas: int, edicion: int):
        super().__init__(fecha, autor, titulo)
        self.paginas = paginas
        self.edicion = edicion

class Articulo:
    def __init__(self, tema: str, autor: str, titulo: str):
        self.tema = tema
        self.autor = autor
        self.titulo = titulo

class Revista(Publicacion):
    def __init__(self, fecha: str, autor: str, titulo: str):
        super().__init__(fecha, autor, titulo)
        self.articulos: list = []

    def __str__(self) -> str:
        titulos = ""
        for articulo in self.articulos:
            titulos +="---"+ articulo.titulo
        return titulos

    def agregar_articulos(self, articulo: Articulo):
        self.articulos.append(articulo)

def main():
    Libro1 = Libro(fecha = "17/08/1945", autor = "George Orwell", titulo = "Rebelion de la granja", paginas = 130, edicion = 3)
    revista = Revista(fecha = "2026/04/22", autor = "Semana", titulo = "Semana")
    articulo1 = Articulo(titulo = "Mision Artemis II", autor = "Yo", tema = "Astronomia")
    articulo2 = Articulo(titulo = "Guerra Iran vs EE. UU with Israel", autor = "usted", tema = "Guerra")
    revista.agregar_articulos(articulo1)
    revista.agregar_articulos(articulo2)

    print(Libro1)
    print(revista)


if __name__ == "__main__":
    main()