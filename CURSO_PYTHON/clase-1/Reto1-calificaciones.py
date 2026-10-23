name = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("ingrese su segunda nota : "))
nota3 = float(input("ingrese su tercera nota: "))
promedio = (nota1 + nota2 + nota3) / 3
print("Su promedio es :", promedio)
if promedio >= 90:
    print("Excelente")
elif promedio >= 71:
    print("pasaste")
else:
    print("te quedaste lol")
