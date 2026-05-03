
import random

numero_secreto = random.randint(1, 10)

while True:
    numero = int(input("Adivina el número (1-10): "))

    if numero == numero_secreto:
        print("¡Correcto!")
        break
    else:
        print("Intenta de nuevo")
