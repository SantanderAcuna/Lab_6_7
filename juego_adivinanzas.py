# Juego de adivinanza
import random
numero_secreto = random.randint(1, 100)
print("¡Adivina el número entre 1 y 100!")
while True:
    intento = int(input("Tu adivinanza: "))
    if intento < numero_secreto:
        print("Es mayor.")
    elif intento > numero_secreto:
        print("Es menor.")
    else:
        print("¡Correcto!")
        break
