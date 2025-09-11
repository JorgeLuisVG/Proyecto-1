class Usuario:
    def __init__(self, Nombre, Codigo):
        self.Nombre = Nombre
        self.Codigo = Codigo


class Estudiante(Usuario):
    def __init__(self, Nombre, Codigo, Grado):
        super().__init__(Nombre, Codigo)
        self.Grado = Grado

class Profesor(Usuario):
    def __init__(self, Nombre, Codigo, Conocimientos):
        super().__init__(Nombre, Codigo)
        self.Conocimientos = Conocimientos 

class Curso:
    def __init__(self, Nombre, Profesor, Estudiantes):
        self.Nombre = Nombre
        self.Profesor = Profesor
        self.Estudiantes = Estudiantes

    def SeleccionarProfesor(self, Lista):
        self.Nombre
        for i in Lista:
            if i[self.Conocimientos] == self.Nombre:
                self.Profesor == i[self.Nombre]

ListaProfesores = []
ListaEstudiantes = []

# MENU
est = input("Ingrese nombre estuduiante")
import random
rnd = random.randint(1000000, 9999999)
grad = input("Ingrese el grado del estudiante")

nuevoEst = Estudiante(est, rnd, grad)

prof = input("Ingrese nombre estuduiante")
rnd2 = random.randint(1000000, 9999999)
conoc = input("Ingrese el area de especialidad del profesor")

NuevoProf = Profesor(prof, rnd, conoc)

Clase = { "Curso": {"Tipo" : "Usuario"}}
