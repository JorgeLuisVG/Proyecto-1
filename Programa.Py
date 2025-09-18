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
        return super().ValidarPin(ProbarPin)
    
class Profesor(Usuario):
    def __init__(self, Nombre, Codigo, Pin, Especialidad):
        super().__init__(Nombre, Codigo, Pin)
        self.Especialidad = Especialidad
    def MostrarInformacion(self):
        super().MostrarInformacion()
        print(f"Especialidad: {self.Especialidad}")
    def ValidarPin(self, ProbarPin):
        return super().ValidarPin(ProbarPin)

class Curso:
    def __init__(self, Nombre, Profesor):
        self.Nombre = Nombre
        self.Profesor = Profesor
        self.Estudiantes = [] # [[Nombre del estudiante, Punteo, [Tareas]]
        self.Tareas = []
        self.PunteoActual = 0

    def actualizarCursos(self, listaDeEstudiantes):
        for est in listaDeEstudiantes:
            if self.Nombre not in est.cursos:
                self.Estudiantes.append([est.Nombre, 0, []])
                est.cursos.append(self.Nombre)
    def Informes(self):
        if self.PunteoActual == 0:
            print("No hay tareas en este curso todavía.")
            return
        Rendimiento = []
        for est in self.Estudiantes:
            if est[1] < 0.55 * self.PunteoActual:
                Rendimiento.append(est)
        print("Estudiantes de bajo rendimiento")
        for i in Rendimiento:
            print(f"Nombre: {i[0]} - Punteo: {i[1]}/{self.PunteoActual}")
        Rendimiento.clear()
        for est in self.Estudiantes:
            if est[1] > 0.80 * self.PunteoActual:
                Rendimiento.append(est)
        print("Estudiantes de alto rendimiento")
        for i in Rendimiento:
            print(f"Nombre: {i[0]} - Punteo: {i[1]}/{self.PunteoActual}")

class Tareas:
    def __init__(self, CursoA, Nombre, explicacion, Valor):
        self.CursoA = CursoA
        self.Nombre = Nombre
        self.Explicacion = explicacion
        self.Valor = Valor
        self.Punteo = None 
        self.Contenido = None
    def AsignarPunteo(self, nota):
        self.Punteo = self.Valor * (nota/100)
    def CompletarTarea(self):
        print("Cumpla las instrucciones de la tarea")
        print(self.Explicacion)
        archivo = input("Ingrese su tarea: ")
        self.Contenido = archivo
    def VerTarea(self):
        print(f"Curso: {self.CursoA}")
        print(f"Tarea: {self.Nombre}, Valor: {self.Valor}")
        print(f"Explicacion: {self.Explicacion}")
        print(f"Entrega: {self.Contenido}")
        print(f"Punteo: {self.Punteo}")

ListaProfesores = []
ListaEstudiantes = []
ListaCursos = []

def TryCatch(listaOpciones):
    while True:
        try:
            opcion = int(input().strip())
        except ValueError:
            print("Ingrese un valor valido")
            continue
        if listaOpciones is None: 
            return opcion
        elif opcion not in listaOpciones:
            print("Ingrese un valor valido")
            continue
        return opcion

def IniciarSesion(lista):
    while True:
        IniciarNombre = input("Ingrese su Nombre ").strip().title()
        for i in lista:
            if i.Nombre == IniciarNombre:
                while True:
                    IniciarContraseña = input("Ingrese su pin ").strip()
                    Validez = i.ValidarPin(IniciarContraseña)
                    if Validez == True:
                        usuario = i
                    else:
                        print("Pin incorrecto")
        if Validez == False: 
            print("No se encontró al usuario intentelo nuevamente")
        elif Validez == True: 
            print("Inicio de sesion Exitoso")
            break
    return usuario

def CrearPin():
    while True:
        Pin = input("Cree su pin de 4 dijitos ").strip()
        if len(Pin) == 4:
            print("Pin valido")
            break
        else: print("Pin invalido")
    return Pin

def Especialidades():
    def Lengua():
        print("Seleccione la Lengua")
        print("1 = Español")
        print("2 = Kiche")
        print("3 = Ingles")
        print("4 = Aleman")
        OpcionLengua = TryCatch([1, 2, 3, 4])
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
    
    OpcionEspecialidad = str(TryCatch([1, 2, 3, 4, 5, 6]))
    
    if OpcionEspecialidad == "4":
        n = Especialidad["4"]()
        return n
    else:
        try:
            return Especialidad[OpcionEspecialidad]
        except KeyError:
            print("Ingrese una opcion correcta")

def Menu():
    while True:
        print("Menu")
        print("1 = Crear Curso")
        print("2 = Ingresar Alumno")
        print("3 = Ingresar profesor")
        print("4 = Crear Tarea")
        print("5 = Inicio de sesion para profesores")
        print("6 = Inicio de sesion para alumnos")
        print("7 = Salir")
        opcion = TryCatch([1, 2, 3, 4, 5, 6, 7])

        if opcion == 1: 
            if not ListaProfesores: 
                print("No hay Profesores cree uno primero")
                continue

            def ElegirProfesor(Lista):
                for i in Lista:
                    i.MostrarInformacion()
                    print()
                eleccion = input("Escriba el código del profesor que desea incluír en este curso ").strip()
                for i in Lista:
                    if i.Codigo == eleccion:
                        return i

            NombreCurso = input("Ingrese el nombre del curso ").strip().title()
            print("Los estudiantes se asignaran de manera automatica")
            print("Seleccione el requisito para el para el profesor del curso")
            requisitos = Especialidades()
            ListaProf2 = []
            for i in ListaProfesores:
                if i.Especialidad == requisitos:
                    ListaProf2.append(i)
            if len(ListaProf2) == 0:
                print("No se encontraron profesores que cumplan con el requisito elija uno entre la lista total")
                Profe = ElegirProfesor(ListaProfesores)
            elif len(ListaProf2) >= 1:
                print("Estos son los profesores que cuentan con el requisito necesario para el curso")
                Profe = ElegirProfesor(ListaProf2)
            Profe.cursos.append(NombreCurso)
            NuevoCurso = Curso(NombreCurso, Profe)
            NuevoCurso.actualizarCursos(ListaEstudiantes)
            ListaCursos.append(NuevoCurso)    
        elif opcion == 2:
            Nombre = input("Ingrese el nombre del estudiante ").strip().title()
            Codigo = random.randint(1000000, 9999999)
            PinEstudiante = CrearPin()
            print(Codigo)

            nuevoEst = Estudiante(Nombre, Codigo, PinEstudiante)
            ListaEstudiantes.append(nuevoEst)
            nuevoEst.MostrarInformacion()
        elif opcion == 3:
            NombreProfesor = input("Ingrese el nombre del profesor ").strip().title()
            Codigo = random.randint(1000000, 9999999)
            Pin = CrearPin()

            print("Ingrese la especialidad del profesor")
            EspecialidadProfesor = Especialidades()

            NuevoProf = Profesor(NombreProfesor, Codigo, Pin, EspecialidadProfesor)
            ListaProfesores.append(NuevoProf)
            NuevoProf.MostrarInformacion()
        elif opcion == 4:
            NombreCursoTarea = input("seleccione el curso a asignar la tarea ").strip().title()
            NombreTarea = input("Ingrese el titulo de la tarea ").strip().title()
            ExplicacionTarea = input("Redacte una explicacion de la tarea ").strip()
            ValorTarea = float(input("Ingrese el valor de la tarea ").strip())
            NuevaTarea = Tareas(NombreCursoTarea, NombreTarea, ExplicacionTarea, ValorTarea)

            for curso in ListaCursos:
                if curso.Nombre == NombreCursoTarea:
                    curso.Tareas.append(NuevaTarea)
                    curso.PunteoActual += ValorTarea
                    for est in curso.Estudiantes:
                        est[2].append(NuevaTarea)      
        elif opcion == 5:
            print("Inicie sesion")
            UsuarioIniciado = IniciarSesion(ListaProfesores)
            while True:
                print("Seleccione la accion que desea realizar")
                print("1 = Calificar Tareas")
                print("2 = Ver informes")
                print("3 = Salir")
                accion = TryCatch([1, 2, 3])
                if accion == 1:
                    for cursoUsuario in UsuarioIniciado.cursos:
                        for curso in ListaCursos:
                            if curso.Nombre == cursoUsuario:
                                print(f"Curso: {curso.Nombre}")
                                for est in curso.Estudiantes:
                                    print(f"Estudiante: {est[0]}")
                                    for tarea in est[2]:
                                        if tarea.Punteo is None: print("No hay tareas")
                                        elif tarea.Punteo is None:
                                            tarea.VerTarea()
                                            print("Asigne un punteo a la tarea sobre el 100% de la calificaion")
                                            nota = TryCatch(None)
                                            tarea.AsignarPunteo(nota)
                                            est[1] += tarea.Punteo
                elif accion == 2:
                    for i in UsuarioIniciado.cursos:
                        for j in ListaCursos:
                            if i == j.Nombre:
                                j.Informes()
                elif accion == 3: 
                    print("Cerrando sesion")
        elif opcion == 6:
            print("Inicie sesion")
            UsuarioIniciado = IniciarSesion(ListaEstudiantes)
            while True:
                print("Seleccione la accion que desea realizar")
                print("1 = Realizar Tareas")
                print("2 = Inscribirse a un nuevo curso")
                print("3 = salir")
                accion = TryCatch([1, 2, 3])

                if accion == 1:
                    for curso in ListaCursos:
                        for estudiante in curso.Estudiantes:
                            if estudiante[0] == UsuarioIniciado.Nombre:
                                for tarea in estudiante[2]:
                                    if tarea.Contenido is None:
                                        tarea.CompletarTarea()
                elif accion == 2:
                    for curso in ListaCursos:
                        encontrado = False
                        for j in UsuarioIniciado.cursos:
                            if  j == curso.Nombre:
                                encontrado = True
                            else: pass
                        if encontrado == False:
                            print(f"Desea añadirse a este curso?: {curso.Nombre}")
                            print("1 = si")
                            print("2 = no")
                            opcion = TryCatch([1, 2])
                            if opcion == 1:
                                curso.Estudiantes.append([UsuarioIniciado.Nombre, 0, []])
                                UsuarioIniciado.cursos.append(curso.Nombre)
                            elif opcion == 2: pass
                        elif encontrado == True: pass
                elif accion == 3:
                    print("Cerrando sesion")
        elif opcion == 7: 
            print("Seguro que desea terminar la ejecucion?")
            print("1 = si")
            print("2 = no")
            salir = TryCatch([1, 2])
            if salir == 1:
                print("Gracias ppor utilizar este programa :)")
                break
            elif opcion == 2:
                pass

Menu()

# est[1] += nota