import re

with open("day03-input.txt", "r") as archivo:
  lista = archivo.readlines()

def simbolo_alrededor(numero):
  

for cadena in lista:
  for numero in re.findall("\d+", cadena):
    if simbolo_alrededor(numero):
      suma += numero
