notas = []
while len(notas) < 5:
    nota = int(input("Porfavor, ingrese sus notas individualmente:"))
    notas.append(nota)
    
suma = sum(notas)
promedio = suma/5

if promedio >= 60:
    print(f"Su promedio es {promedio}, usted ha aprobado la materia")
elif promedio < 60 and promedio >= 40:
    print(f"Su promedio es {promedio}, usted actualmente se encuentra en recuperación")
else:
    print(f"Su promedio es {promedio}, usted ha reprobado")
