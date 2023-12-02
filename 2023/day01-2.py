with open("day01-input.txt", "r") as archivo:
  lista = archivo.readlines()

suma = 0
cardinales = ["one","two","three","four","five","six","seven","eight","nine"]

for cadena in lista:
  numeros = []
  for i, caracter in enumerate(cadena):
    if ord(caracter)>=49 and ord(caracter)<=57 : # si es número
      numeros.append(caracter)
    else:
      for j, cardinal in enumerate(cardinales): # veamos si hay algún cardinal
        if cadena[i:i+len(cardinal)] == cardinal :
          numeros.append(str(j+1))
  suma += int(numeros[0] + numeros[-1]) # sumamos el número formado por el primer y último dígito en "numeros"

print(suma)
