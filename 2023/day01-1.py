import re

with open("day01-input.txt", "r") as archivo:
  lista = archivo.readlines()

suma = 0

for cadena in lista:
  primer_digito = re.search(r"\d", cadena)
  ultimo_digito = re.search(r"\d", cadena[::-1]) # [::-1] invierte el string
  numero = int(primer_digito.group() + ultimo_digito.group()) # match > string > une strings > integer
  suma += numero

print(suma)
