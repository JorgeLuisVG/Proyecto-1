class Usuario():
    def __init__(self, Nombre, Codigo, Id):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Id = Id

class Estudiante(Usuario):
    def __init__(self, Nombre, Codigo, Id, Grado):
        super().__init__(Nombre, Codigo, Id)
        self.Grado = Grado

class Profesor(Usuario):
    def __init__(self, Nombre, Codigo, Id, Conocimientos):
        super().__init__(Nombre, Codigo, Id)
        self.Conocimientos = Conocimientos 

