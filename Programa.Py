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
        elif OpcionNivel == 2:
            opcionGrado = input()
            if opcionGrado == 1:
                return "Primero Basico"
            elif opcionGrado == 2:
                return "Segundo Basico"
            elif opcionGrado == 3:
                return "Tercero Basico"
        elif OpcionNivel == 3:
            opcionGrado = input()
            if opcionGrado == 1:
                return "Primer grado de nivel Diversificado"
            elif opcionGrado == 2:
                return "Segundo grado de nivel Diversificado"
            elif opcionGrado == 3:
                return "Tercer grado de nivel Diversificado"

    def Especialidades():
        def Lengua():
            print("Seleccione la Lengua:")
            print("1 = Español")
            print("2 = Kiche")
            print("3 = Ingles")
            print("4 = Aleman")
            while True:
                try:
                    OpcionLengua = int(input())
                except ValueError:
                    print("ingrese una opcion valida")
                else: break
            if OpcionLengua == 1:
                return "Lenguaje Español"
            elif OpcionLengua == 2:
                return "Lenguaje Kiche"
            elif OpcionLengua == 3:
                return "Lenguaje Ingles"
            elif OpcionLengua == 4:
                return "Lenguaje Aleman"
        Especialidad = {
            "1" : "Matematicas",
            "2" : "Programacion",
            "3" : "Ciencias",
            "4" : Lengua,
            "5" : "Filosofía",
            "6" : "Actividad Fisica"
        }
        for i, j  in Especialidad.items():
            if i == "4":
                print(f"numero: {i}, Especialidad: Lengua")
            else:
                print(f"numero: {i}, Especialidad: {j}")
        while True:
            try:
                OpcionEspecialidad = int(input("Ingrese una opcion"))
            except ValueError:
                print("Ingrese una opcion valida")
            else: break
        OpcionEspecialidad= str(OpcionEspecialidad)
        
        if OpcionEspecialidad == "4":
            n = Especialidad["4"]()
            return n
        else:
            try:
                return Especialidad[OpcionEspecialidad]
            except KeyError:
                print("Ingrese una opcion correcta")

    print("Menu")
    print("1 = Ingresar profesor")
    print("2 = Ingresar Alumno")
    print("3 = Crear Curso")
    print("4 = Ingresar profesor")
    opcion = int(input("Seleccione una opcion"))

    if opcion == 1: 
        NombreProfesor = input("Ingrese el nombre del profesor")
        Codigo = random.randint(1000000, 9999999)
        print("Ingrese la especialidad del profesor")
        EspecialidadProfesor = Especialidades()

        NuevoProf = Profesor(NombreProfesor, Codigo, EspecialidadProfesor)
        NuevoProf.MostrarInformacion()
    elif opcion == 2:
        Nombre = input("Ingrese el nombre del estudiante")
        Codigo = random.randint(1000000, 9999999)
        Grado = DefinirGrado()

        nuevoEst = Estudiante(Nombre, Codigo, Grado)
        nuevoEst.MostrarInformacion()
    elif opcion == 3:
        print()
    elif opcion == 4:
        print()

Menu()

ListaProfesores = []
ListaEstudiantes = []