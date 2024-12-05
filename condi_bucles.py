# Determinar si un número es par o impar
numero = int(input("Ingresa un número: "))
if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Iterar sobre una lista de números e imprimir sus cuadrados
numeros = [1, 2, 3, 4, 5]
for n in numeros:
    print(f"El cuadrado de {n} es {n**2}")

# Bucle while que solicita un número hasta que se ingrese el 0
while True:
    entrada = int(input("Ingresa un número (0 para salir): "))
    if entrada == 0:
        print("¡Gracias por participar!")
        break
    print(f"Ingresaste: {entrada}")
