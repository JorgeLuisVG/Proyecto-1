import random
class Usuario:
    def __init__(self, Nombre, Codigo, Pin):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.cursos = []
        self.__Pin = Pin
    def MostrarInformacion(self):
        print(f"Nombre: {self.Nombre}, Codigo: {self.Codigo}")
        for i in self.cursos:
            print(i)
    def ValidarPin(self, ProbarPin):
        if ProbarPin == self.__Pin:
            return True
        else: return False

class Estudiante(Usuario):
    def __init__(self, Nombre, Codigo, Pin):
        super().__init__(Nombre, Codigo, Pin)
        self.ListaTareas = []
    def MostrarInformacion(self):
        super().MostrarInformacion()
    def ValidarPin(self, ProbarPin):
        super().ValidarPin(ProbarPin)
class Profesor(Usuario):
    def __init__(self, Nombre, Codigo, Pin, Especialidad):
        super().__init__(Nombre, Codigo, Pin)
        self.Especialidad = Especialidad
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Especialidad: {self.Especialidad}")

class Curso:
    def __init__(self, Nombre, Profesor):
        self.Nombre = Nombre
        self.Profesor = Profesor
        self.Estudiantes = []
        self.TareasCalificar = []
    def actualizarCursos(self, Lista):
        for i in Lista:
            for j in i.cursos:
                if j == self.Nombre:
                    pass
                elif j == self.Nombre:
                    self.Estudiantes.append(i.Nombre)
                    i.cursos.append(self.Nombre)
class Tareas:
    def __init__(self, CursoA, Nombre, explicacion, Valor):
        self.CursoA = CursoA
        self.Nombre = Nombre
        self.Explicacion = explicacion
        self.Valor = Valor
        self.Punteo = 0 
        self.Contenido = ""
    def AsignarPunteo(self, nota):
        self.Punteo = self.Valor * nota
    def CompletarTarea(self):
        print("Cumpla las instrucciones de la tarea")
        print(self.Explicacion)
        archivo = input()
        self.contenido = archivo
    def VerTarea(self):
        print(f"Curso: {self.CursoA}")
        print(f"Tarea: {self.Nombre}, Valor: {self.Valor}")
        print(f"Explicacion: {self.Explicacion}")
        print(f"Entrega: {self.Contenido}")
        if self.Punteo == 0:
            print("Tarea Por Calificar")
            self.AsignarPunteo()

ListaProfesores = []
ListaEstudiantes = []
ListaCursos = []

def IniciarSesion():
    IniciarNombre = input("Ingrese su Nombre Completo")
    IniciarContraseña = input("Ingrese su pin")

def Menu():
    def Especialidades():
        def Lengua():
            print("Seleccione la Lengua")
            print("1 = Español")
            print("2 = Kiche")
            print("3 = Ingles")
            print("4 = Aleman")
            while True:
                try:
                    OpcionLengua = int(input().strip())
                except ValueError:
                    print("ingrese una opcion valida")
                else: break
            if OpcionLengua == 1: return "Lenguaje Español"
            elif OpcionLengua == 2: return "Lenguaje Kiche"
            elif OpcionLengua == 3: return "Lenguaje Ingles"
            elif OpcionLengua == 4: return "Lenguaje Aleman"
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
                OpcionEspecialidad = int(input("Ingrese una opcion").strip())
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

    def CrearPin():
        Pin = int(input("Cree su pin de 4 dijitos").strip())
        while True:
            if len(Pin) == 4:
                print("Pin valido")
                break
            else: print("Pin invalido")
        return Pin
    
    print("Menu")
    print("1 = Crear Curso")
    print("2 = Ingresar Alumno")
    print("3 = Ingresar profesor")
    print("5 = Crear Tarea")
    while True:
        try:
            opcion = int(input("Seleccione una opcion")).strip()
        except ValueError: 
            print("Ingrese una opcion valida")
        else: break

    if opcion == 1: 
        def ElegirProfesor(Lista):
            for i in Lista:
                i.MostrarInformacion()
                print()
            eleccion = input("Escriba el código del profesor que desea incluír en este curso").strip()
            for i in Lista:
                if i.Codigo == eleccion:
                    return i

        NombreCurso = input("Ingrese el nombre del curso").strip().title()
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
        NuevoCurso.actualizarCursos(ListaEstudiantes)
        ListaCursos.append(NuevoCurso)    
    elif opcion == 2:
        Nombre = input("Ingrese el nombre del estudiante").strip().title()
        Codigo = random.randint(1000000, 9999999)
        PinEstudiante = CrearPin()

        nuevoEst = Estudiante(Nombre, Codigo, PinEstudiante)
        ListaEstudiantes.append(nuevoEst)
        nuevoEst.MostrarInformacion()
        
    elif opcion == 3:
        NombreProfesor = input("Ingrese el nombre del profesor").strip().title()
        Codigo = random.randint(1000000, 9999999)

        print("Ingrese la especialidad del profesor")
        EspecialidadProfesor = Especialidades()

        NuevoProf = Profesor(NombreProfesor, Codigo, EspecialidadProfesor)
        ListaProfesores.append(NuevoProf)
        NuevoProf.MostrarInformacion()
    elif opcion == 4:
        NombreCursoTarea = input("seleccione el curso a asignar la tarea")
        NombreTarea = input("Ingrese el titulo de la tarea")
        ExplicacionTarea = input("Redacte una explicacion de la tarea")
        ValorTarea = input("Ingrese el valor de la tarea")
        NuevaTarea = Tareas(NombreTarea, ExplicacionTarea, ValorTarea)

Menu()
