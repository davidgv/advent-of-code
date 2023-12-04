import re

with open("day02-input.txt", "r") as archivo:
  lista_archivo = archivo.readlines()

potencia = 0

for cadena in lista_archivo:
  minimos = [0, 0, 0] # array de minimos [red, green, blue]
  game = re.findall(r"(\d+) (\w+)", cadena)

  for par in game:
    if (par[1] == "red") and (int(par[0]) > minimos[0]) :
        minimos[0] = int(par[0])
    if (par[1] == "green") and (int(par[0]) > minimos[1]) :
        minimos[1] = int(par[0])
    if (par[1] == "blue") and (int(par[0]) > minimos[2]) :
        minimos[2] = int(par[0])

  potencia += (minimos[0] * minimos[1] * minimos[2])

print(potencia)