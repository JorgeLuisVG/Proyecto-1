import random
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


def Menu():
    print("Menu")
    print("1 = Ingresar profesor")
    print("2 = Ingresar Alumno")
    print("3 = Crear Curso")
    print("4 = Ingresar profesor")
    opcion = input("Seleccione una opcion")

    if opcion == 1: 
        print()
    elif opcion == 2:
        def DefinirGrado():
            def DefinirNivGrad():
                print("Ingrese el grado")
                print("1 = Primero")
                print("2 = segundo")
                print("3 = Tercero")
            print("Ingrese el nivel Academico")
            print("1 = Primaria")
            print("2 = Basico")
            print("3 = Diversificado")
            OpcionNivel = input()

            DefinirNivGrad()
            if OpcionNivel == 1:
                print("4 = Cuarto")
                print("5 = Quinto")
                print("6 = Sexto")
                opcionGrado = input()

                if opcionGrado == 1:
                    return "Primero Primaria"
                elif opcionGrado == 2:
                    return "Segundo Primaria"
                elif opcionGrado == 3:
                    return "Tercero Primaria"
                elif opcionGrado == 4:
                    return "Cuarto Primaria"
                elif opcionGrado == 5:
                    return "Quinto Primaria"
                elif opcionGrado == 6:
                    return "Sexto Primaria"

        Nombre = input("Ingrese nombre estuduiante")
        Codigo = random.randint(1000000, 9999999)
        Grado = input("Ingrese el grado del estudiante")

        nuevoEst = Estudiante(est, rnd, grad)
        nuevoEst.MostrarInformacion()
    elif opcion == 3:
        print()
    elif opcion == 4:
        print()

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
