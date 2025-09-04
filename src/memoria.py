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
    calificaciones[curso]=0
#usuario puede añadir valores al diccionario
for curso in cursos:
    nota = int(input(f"digite la nota del estudiante {estudiante} de la materia {curso}: "))
    calificaciones[curso] = nota


promedio = 0
for curso in cursos:
    promedio += calificaciones[curso]
promedio = promedio/len(cursos)
print(f"el promedio general del estudiante {estudiante} es: {promedio}")
