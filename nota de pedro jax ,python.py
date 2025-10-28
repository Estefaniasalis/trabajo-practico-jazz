nota1 = float(input("sea bienvenido/a")
nota2 = float(input("Ingresa la primera nota por favor: "))
nota3 = float(input("Ingresa la segunda nota por favor: "))
promedio = (nota1 + nota2) / 2
nombre = input("Ingresa el nombre del alumno/a por favor: ")
print(f"El promedio de {nombre} es {promedio}")
notas_aprobadas = [6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10]
aprobo = promedio in notas_aprobadas
print(f"¿{nombre} aprobó la materia? {aprobo}")

