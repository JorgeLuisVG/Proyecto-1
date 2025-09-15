import random
class Usuario:
    def __init__(self, Nombre, Codigo):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.cursos = []
    
    def MostrarInformacion(self):
        print(f"Nombre: {self.Nombre}, Codigo: {self.Codigo}")
        for i in self.cursos:
            print(i)
        
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
        self.curso = ""
    
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Especialidad: {self.Especialidad}")

class Curso:
    def __init__(self, Nombre, Profesor):
        self.Nombre = Nombre
        self.Profesor = Profesor
        self.Estudiantes = []
    def AñadirEstudiantes(self, Lista):
        for i in Lista:
            for j in i.Cursos:
                if j == self.Nombre:
                    self.Estudiantes.append()
                else: continue
class Tareas:
    def __init__(self, Nombre, explicacion, Valor):
        self.Nombre = Nombre
        self.Explicacion = explicacion
        self.Valor = Valor
        self.Punteo : float
    def AsignarPunteo(self, nota):
        self.Punteo = self.Valor * nota

ListaProfesores = []
ListaEstudiantes = []
ListaCursos = []

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
    print("1 = Crear Curso")
    print("2 = Ingresar Alumno")
    print("3 = Ingresar profesor")
    print("4 = Ingresar profesor")
    print("5 = Crear Tarea")
    while True:
        try:
            opcion = int(input("Seleccione una opcion"))
        except ValueError: 
            print("Ingrese una opcion valida")
        else: break

    if opcion == 1: 
        def ElegirProfesor(Lista):
            for i in Lista:
                i.MostrarIndormacion()
                print()
            eleccion = input("Escriba el código del profesor que desea incluír en este curso")
            for i in Lista:
                if i.Codigo == eleccion:
                    return i

        NombreCurso = input("Ingrese el nombre del curso")
        print("Los estudiantes se asignaran de manera automatica")
        print("Seleccione el requisito para el para el profesor del curso")
        requisitos = Especialidades()
        encontrado = None
        ListaProf2 = []
        for i in ListaProfesores:
            if i.Especialidad== requisitos:
                ListaProf2.append(i)
        if len(ListaProf2) == 0:
            print("No se encontraron profesores que cumplan con el requisito elija uno entre la lista total")
            Profe = ElegirProfesor(ListaProfesores)
        elif len(ListaProf2) >= 1:
            print("Estos son los profesores que cuentan con el requisito necesario para el curso")
            Profe = ElegirProfesor(ListaProf2)
        NuevoCurso = Curso(NombreCurso, Profe)
        ListaCursos.append(NuevoCurso)
    elif opcion == 2:
        Nombre = input("Ingrese el nombre del estudiante")
        Codigo = random.randint(1000000, 9999999)
        Grado = DefinirGrado()

        nuevoEst = Estudiante(Nombre, Codigo, Grado)
        ListaEstudiantes.append(nuevoEst)
        nuevoEst.MostrarInformacion()
    elif opcion == 3:
        NombreProfesor = input("Ingrese el nombre del profesor")
        Codigo = random.randint(1000000, 9999999)
        print("Ingrese la especialidad del profesor")
        EspecialidadProfesor = Especialidades()

        NuevoProf = Profesor(NombreProfesor, Codigo, EspecialidadProfesor)
        ListaProfesores.append(NuevoProf)
        NuevoProf.MostrarInformacion()
    elif opcion == 4:
        print()
    elif opcion == 5:
        NombreTarea = input("Ingrese el titulo de la tarea")
        ExplicacionTarea = input("Redacte una explicacion de la tarea")
        ValorTarea = input("Ingrese el valor de la tarea")
        NuevaTarea = Tareas(NombreTarea, ExplicacionTarea, ValorTarea)

Menu()
