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
        self.Estudiantes = [] # [[Nombre del estudiante, Punteo, [Tareas], [Evaluaciones]]
        self.Tareas = []
        self.PunteoActual = 0

    def actualizarCursos(self, listaDeEstudiantes):
        for est in listaDeEstudiantes:
            if self.Nombre not in est.cursos:
                self.Estudiantes.append([est.Nombre, 0, [], []])
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

class Evaluacion:
    def __init__(self, Nombre, valor):
        self.Nombre = Nombre
        self.Nota = None
        self.Valor = valor
        self.preguntas = []
        self.Resuelto = False
    def IngresarPreguntas(self):
        while True:
            pregunta = input("Ingrese una pregunta: ").strip()
            self.preguntas.append([pregunta, None])
            print("Desea ingresar otra pregunta? (1 = si, 2 = no): ")
            Salir = TryCatch([1, 2])
            if Salir == 1:
                continue
            elif Salir == 2:
                break    
    def RendirExamen(self):
        for pregunta in self.preguntas:
            print(f"Pregunta: {pregunta[0]}")
            pregunta[1] = input("ingrese su prepuesta").strip()
        print("Evaluacion Terminada")
        self.Resuelto = True
    def VerResolucion(self):
        for pregunta in self.preguntas:
            print(f"Pregunta: {pregunta[0]}")
            print(f"Respuesta: {pregunta[1]}")
        print("Que calificacion le da a esta evaluacion sobre el 100% del punteo?: ")
        self.Nota = TryCatch(None)

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
    Validez = False
    while True:
        IniciarNombre = input("Ingrese su Nombre ").strip().title()
        for i in lista:
            if i.Nombre == IniciarNombre:
                while True:
                    IniciarContraseña = input("Ingrese su pin: ").strip()
                    Validez = i.ValidarPin(IniciarContraseña)
                    if Validez == True:
                        usuario = i
                        break
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

            NombreCurso = input("Ingrese el nombre del curso ").strip().title()
            print("Los estudiantes se asignaran de manera automatica")
            print("Seleccione el requisito para el para el profesor del curso")
            requisitos = Especialidades()

            candidatos = []
            for p in ListaProfesores:
                if p.Especialidad == requisitos:
                    candidatos.append(p)
            if not candidatos:
                print("No hay profesores con esa especialidad. Mostrando todos:")
                candidatos = ListaProfesores
            for p in candidatos:
                p.MostrarInformacion()
            Profe = None
            while True:
                print("Ingrese el codigo del profesor seleccionado")
                codigo = TryCatch(None)

                for p in candidatos:
                    if p.Codigo == codigo:
                        Profe = p
                    break
                if Profe is None:
                    print("Ingrese un codigo valido")
                elif Profe != None:
                    print("Profesor seleccionado con exito")
                    break
            
            Profe.cursos.append(NombreCurso)
            NuevoCurso = Curso(NombreCurso, Profe)
            NuevoCurso.actualizarCursos(ListaEstudiantes)
            ListaCursos.append(NuevoCurso)
            print(f"El curso: {NombreCurso} fue creado con exito")  
        elif opcion == 2:
            Nombre = input("Ingrese el nombre del estudiante: ").strip().title()
            Codigo = random.randint(1000000, 9999999)
            PinEstudiante = CrearPin()
            print(Codigo)

            nuevoEst = Estudiante(Nombre, Codigo, PinEstudiante)
            ListaEstudiantes.append(nuevoEst)
            print("Estudiante registrado con exito")
            nuevoEst.MostrarInformacion()
        elif opcion == 3:
            NombreProfesor = input("Ingrese el nombre del profesor: ").strip().title()
            Codigo = random.randint(1000000, 9999999)
            Pin = CrearPin()

            print("Ingrese la especialidad del profesor")
            EspecialidadProfesor = Especialidades()

            NuevoProf = Profesor(NombreProfesor, Codigo, Pin, EspecialidadProfesor)
            ListaProfesores.append(NuevoProf)
            print("Profesor registrado con exito")
            NuevoProf.MostrarInformacion()
        elif opcion == 4:
            NombreCursoTarea = input("seleccione el curso a asignar la tarea: ").strip().title()
            curso = None
            for c in ListaCursos:
                if c.Nombre == NombreCursoTarea:
                    curso = c
            if curso is None:
                print("Curso no encontrado.")
                continue
            NombreTarea = input("Ingrese el titulo de la tarea: ").strip().title()
            ExplicacionTarea = input("Redacte una explicacion de la tarea: ").strip()
            ValorTarea = float(input("Ingrese el valor de la tarea: ").strip())
            NuevaTarea = Tareas(NombreCursoTarea, NombreTarea, ExplicacionTarea, ValorTarea)

            curso.Tareas.append(NuevaTarea)
            curso.PunteoActual += ValorTarea
            for est in curso.Estudiantes:
                est[2].append(NuevaTarea)
            print("Tarea creada y asignada a los estudiantes.")
        elif opcion == 5:
            print("Inicie sesion")
            UsuarioIniciado = IniciarSesion(ListaProfesores)
            while True:
                print("Seleccione la accion que desea realizar")
                print("1 = Calificar Tareas")
                print("2 = Ver informes")
                print("3 = Asignar evaluacion")
                print("4 = Calificar Evaluaciones")
                print("5 = Salir")
                accion = TryCatch([1, 2, 3, 4, 5])
                if accion == 1:
                    for curso in ListaCursos:
                        if curso.Nombre in UsuarioIniciado.cursos:
                            print(f"Curso: {curso.Nombre}")
                            for est in curso.Estudiantes:
                                print(f"Estudiante: {est[0]}")
                                for tarea in est[2]:
                                    if tarea.Punteo is None:
                                        tarea.VerTarea()
                                        print("Nota (0-100):")
                                        nota = TryCatch(None)
                                        tarea.AsignarPunteo(nota)
                                        est[1] += tarea.Punteo
                elif accion == 2:
                    for curso in ListaCursos:
                        if curso.Nombre in UsuarioIniciado.cursos:
                            curso.Informes()
                elif accion == 3:
                    paraCurso = input("Ingrese el curso para el que asignara la Evaluacion: ").strip().title()
                    if paraCurso in UsuarioIniciado.cursos:
                        nombreEvaluacion = input("Ingrese el nombre de la evaluacion: ")
                        valorevaluacion = float(input("Ingrese el valor de la evaluacion: "))

                        NuevaEvaluacion = Evaluacion(nombreEvaluacion, valorevaluacion)
                        NuevaEvaluacion.IngresarPreguntas()
                        for curso in ListaCursos:
                            if curso.Nombre == paraCurso:
                                curso.PunteoActual += valorevaluacion
                                for estud in curso.Estudiantes:
                                    estud[3].append(NuevaEvaluacion)
                elif accion == 4:
                    for curso in ListaCursos:
                        if curso.Nombre in UsuarioIniciado.cursos:
                            print(f"Curso: {curso.Nombre}")
                            for est in curso.Estudiantes:
                                print(f"Estudiante: {est[0]}")
                                for evaluacion in est[3]:
                                    if evaluacion.Nota is None:
                                        evaluacion.VerResolucion()
                                        est[1] += evaluacion.Nota
                elif accion == 5: 
                    print("Cerrando sesion")
                    break
        elif opcion == 6:
            print("Inicie sesion")
            UsuarioIniciado = IniciarSesion(ListaEstudiantes)
            while True:
                print("Seleccione la accion que desea realizar")
                print("1 = Realizar Tareas")
                print("2 = Inscribirse a un nuevo curso")
                print("3 = Rendir Evaluaciones")
                print("4 = salir")
                accion = TryCatch([1, 2, 3, 4])

                if accion == 1:
                    for curso in ListaCursos:
                        for estudiante in curso.Estudiantes:
                            if estudiante[0] == UsuarioIniciado.Nombre:
                                for tarea in estudiante[2]:
                                    if tarea.Contenido is None:
                                        tarea.CompletarTarea()
                elif accion == 2:
                    for curso in ListaCursos:
                        if curso.Nombre not in UsuarioIniciado.cursos:
                            print(f"Desea añadirse a este curso?: {curso.Nombre}")
                            print("1 = si")
                            print("2 = no")
                            añadir = TryCatch([1, 2])
                            if añadir == 1:
                                curso.Estudiantes.append([UsuarioIniciado.Nombre, 0, [], []])
                                UsuarioIniciado.cursos.append(curso.Nombre)
                                print(f"{UsuarioIniciado.Nombre} inscrito en {curso.Nombre}")
                elif accion == 3:
                    for curso in ListaCursos:
                        for estudiante in curso.Estudiantes:
                            if estudiante[0] == UsuarioIniciado.Nombre:
                                for examen in estudiante[3]:
                                    if examen.Resuelto is False:
                                       examen.RendirExamen()
                elif accion == 4:
                    print("Cerrando sesion")
                    break
        elif opcion == 7: 
            print("Seguro que desea terminar la ejecucion?")
            print("1 = si")
            print("2 = no")
            salir = TryCatch([1, 2])
            if salir == 1:
                print("Gracias ppor utilizar este programa :)")
                break
            elif opcion == 2:
                continue
Menu()