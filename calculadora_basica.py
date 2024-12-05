# Calculadora básica
print("Calculadora Básica")
print("1: Sumar, 2: Restar, 3: Multiplicar, 4: Dividir")
opcion = int(input("Selecciona una opción: "))
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == 1:
    print(f"La suma es: {num1 + num2}")
elif opcion == 2:
    print(f"La resta es: {num1 - num2}")
elif opcion == 3:
    print(f"El producto es: {num1 * num2}")
elif opcion == 4 and num2 != 0:
    print(f"El cociente es: {num1 / num2}")
else:
    print("Opción inválida o división por cero.")

