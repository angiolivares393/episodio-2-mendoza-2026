import random

intentos = 3

numeroAleatorio = random.randint(1, 10)

numeroUsuario = int(input("Ingrese su numero: "))

while(intentos > 0 and numeroAleatorio != numeroUsuario):
    print("Numero Incorrecto")
    numeroUsuario = int(input("volve a ingresar un numero: "))
    intentos = intentos -1


if(numeroUsuario == numeroAleatorio):
    print("¡correcto!")

if(intentos == 0):
    print("sin intentos restantes")

=====================================================================

print: 

