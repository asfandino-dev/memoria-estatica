#############################################################################################
# Universidad de Cundinamarca                                                               #
# Autor: Adner Santiago Fandiño Gonzalez                                                    #
# gitHub: asfandino-dev                                                                     #
# Materia: Estructuras de Informacion                                                       #
# Objetivo: comprender el uso de memoria estatica e inmutable y memoria dinamica y mutable  #
#############################################################################################

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
#usuario puede añadir valores al diccionario y la lista dentro del diccionario
for curso in cursos:
    nota = int(input(f"digite la nota del estudiante {estudiante} de la materia {curso}: "))
    calificaciones[curso].append(nota)

#agregar notas
cursoNota = str(input(f"digita el nombre del curso para agregar la nota: {cursos}"))
if cursoNota in cursos:
    nuevaNota = int(input("Digite la nueva nota"))
    calificaciones[cursoNota].append(nuevaNota)
    print(f"las notas de la materia {cursoNota} del estudiante {estudiante} es: {calificaciones[cursoNota]}")
else:
    print("digite un curso valido")

#modificar notas
print(f"selecciones el curso para modificar la nota: {cursos}")
modificar = str(input("digita el nombre del curso para modificar la nota: "))
if modificar in cursos:
    notaM = int(input(f"las notas acuales del curso {modificar} son: {calificaciones[modificar]}\npor favor seleccione la posicion de la nota a modificar (1,2,3 etc)"))
    calificaciones[modificar].pop(notaM-1)
    nueva_nota = int(input("digite la nueva nota"))
    calificaciones[modificar].append(nueva_nota)
else:
    print("no seleccionaste un curso valido")

#eliminar notas
print(f"selecciones el curso para eliminar la nota: {cursos}")
modificar = str(input("digita el nombre del curso para eliminar la nota: "))
if modificar in cursos:
    notaM = int(input(f"las notas acuales del curso {modificar} son: {calificaciones[modificar]}\npor favor seleccione la posicion de la nota a eliminar (1,2,3 etc)"))
    calificaciones[modificar].pop(notaM-1)
    calificaciones[modificar].append(0)
    print(f"las notas actuales del curso {modificar} son: {calificaciones[modificar]}")
else:
    print("no seleccionaste un curso valido")

#promedio de notas
suma_total = 0
contador_total = 0

for curso in cursos:
    suma_total += sum(calificaciones[curso])       # sumamos todas las notas de ese curso
    contador_total += len(calificaciones[curso])   # contamos cuántas notas tenía ese curso
print(suma_total, contador_total)
promedio = suma_total / contador_total
print(f"Las notas actuales del {estudiante} es: {calificaciones}")
print(f"El promedio general del estudiante {estudiante} es: {promedio}")

