for letra in "Angelina":
    print (letra)
print("===============================================")
for numeros in range(1,11):
    print (numeros)
print("==============================================")
for numeros in range(200,301, 2):
    print (numeros)
print ("=============================================")
for numeros in range(10,0,-1):
    print (numeros) 
print ("DESPEGUE")
numero = 4
print("==============================================")
for valor in range (1, 11):
    resultado = numero * valor 
    print (f"{numero} X {valor} = {resultado}")
print("==============================================")
numero = 6
notas = [10,4]
sumatoria = 0
for nota in notas:
    sumatoria += nota #sumatoria = sumatoria + nota 

promedio = sumatoria / len (notas)
print("El promedio es:",promedio)
print("===============================================")
precios = [200, 500, 1200, 13500, 5000]
for precio in precios:
    precioConDescuento = precio *0.8
    print (f"ELprecio del producto es${precio} y con el descuento es: $[]