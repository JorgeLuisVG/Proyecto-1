class Usuario:
    def __init__(self, Nombre, Codigo):
        self.Nombre = Nombre
        self.Codigo = Codigo
    
    def MostrarInformacion(self):
        print(f"Nombre: {self.Nombre}, Codigo: {self.Codigo}")
        
class Estudiante(Usuario):
    def __init__(self, Nombre, Codigo, Grado):
        super().__init__(Nombre, Codigo)
        self.Grado = Grado
    
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(self.Grado)


class Profesor(Usuario):
    def __init__(self, Nombre, Codigo, Especialidad):
        super().__init__(Nombre, Codigo)
        self.Especialidad = Especialidad
    
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Especialidad: {self.Especialidad}")


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
nuevoEst.MostrarInformacion()

prof = input("Ingrese nombre estuduiante")
rnd2 = random.randint(1000000, 9999999)
conoc = input("Ingrese el area de especialidad del profesor")

NuevoProf = Profesor(prof, rnd, conoc)
NuevoProf.MostrarInformacion()

Clase = { "Curso": {"Tipo" : "Usuario"}}
