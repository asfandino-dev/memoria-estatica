#############################################################################################
# Universidad de Cundinamarca                                                               #
# Autor: Adner Santiago Fandiño Gonzalez                                                    #
# gitHub: asfandino-dev                                                                     #
# Materia: Estructuras de Informacion                                                       #
# Objetivo: comprender el uso de memoria estatica e inmutable y memoria dinamica y mutable  #
#############################################################################################

#agregar notas
def agregarNotas():
    cursoNota = str(input(f"digita el nombre del curso para agregar la nota: {cursos} "))
    if cursoNota in cursos:
        nuevaNota = int(input("Digite la nueva nota: "))
        calificaciones[cursoNota].append(nuevaNota)
        print(f"las notas de la materia {cursoNota} del estudiante {estudiante} es: {calificaciones[cursoNota]}")
    else:
        print("digite un curso valido")    

#modificar notas
def modificarNotas():

    print(f"selecciones el curso para modificar la nota: {cursos}")
    modificar = str(input("digita el nombre del curso para modificar la nota: "))
    if modificar in cursos:
        notaM = int(input(f"las notas acuales del curso {modificar} son: {calificaciones[modificar]}\npor favor seleccione la posicion de la nota a modificar (1,2,3 etc): "))
        nueva_nota = int(input("digite la nueva nota: "))
        calificaciones[modificar][notaM-1] = nueva_nota
    else:
        print("no seleccionaste un curso valido")


#eliminar notas
def eliminarNotas():
    print(f"selecciones el curso para eliminar la nota: {cursos}")
    modificar = str(input("digita el nombre del curso para eliminar la nota: "))
    if modificar in cursos:
        notaM = int(input(f"las notas acuales del curso {modificar} son: {calificaciones[modificar]}\npor favor seleccione la posicion de la nota a eliminar (1,2,3 etc): "))
        calificaciones[modificar][notaM-1] = 0
        print(f"las notas actuales del curso {modificar} son: {calificaciones[modificar]}")
    else:
        print("no seleccionaste un curso valido")

#promedio de notas
def promedio():
    suma_total = 0
    contador_total = 0

    for curso in cursos:
        suma_total += sum(calificaciones[curso])       # sumamos todas las notas de ese curso
        contador_total += len(calificaciones[curso])   # contamos cuántas notas tenía ese curso
    print(suma_total, contador_total)
    promedio = suma_total / contador_total
    print(f"Las notas actuales del {estudiante} es: {calificaciones}")
    print(f"El promedio general del estudiante {estudiante} es: {promedio}")

#Variables inmutables ya que no se pueden modificar y si se modifican se estará creando otra variable en memoria
#tupla
cursos = ("calculo", "estructuras", "fisica")
#variable tipo str
estudiante = "santiago fandiño"

#variables mutables ya que se pueden modificar y no cambiará su direccion de memoria
#diccionario
calificaciones ={}

#añadiendo valores iniciales al diccionario
for curso in cursos:
    calificaciones[curso]=[]
    
print("Bienvenido")
opcion = 0
while True:
    opcion = int(input("Por favor selecicones una de las opciones:\n1.Añadir calificaciones\n2.modificar calificaciones\n3.Eliminar calificaciones\n4.Promedio general\nSi desea finzalizar por favor digite otro numero: "))
    if opcion == 1:
        agregarNotas()
    elif opcion == 2:
        modificarNotas()
    elif opcion == 3:
        eliminarNotas()
    elif opcion == 4:
        promedio()
    else:
        print("Saliendo del programa...")
        break
