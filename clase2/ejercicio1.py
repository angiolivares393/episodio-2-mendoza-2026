nombre = input("Cual es el nombre de tu personaje? ")
clase = input("que clase es tu personaje? ")
raza = input("que raza es tu personaje? ")
nivel = int (input("que nivel es tu personaje? "))
vida = nivel *10
destresa = int(input("cual es su desestresa? "))
armadura = destresa *10



print("===== Hoja de personaje ======")
print("Nombre:", nombre)
print("clase:", clase)
print("raza:", raza)
print("nivel", nivel)
print("vida", vida)
print("armadura", armadura)