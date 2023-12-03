import re

with open("day02-input.txt", "r") as archivo:
  lista_archivo = archivo.readlines()

suma = 0
lista_games = []

for cadena in lista_archivo:
  game = re.findall(r"(\d+) (\w+)", cadena)
  imposible = False
  for par in game:
    if par[1] == "red":
      if int(par[0]) > 12:
        imposible = True # no puede tener más de 12 cubos rojos
        break
    if par[1] == "green":
      if int(par[0]) > 13:
        imposible = True # no puede tener más de 13 cubos verdes
        break
    if par[1] == "blue":
      if int(par[0]) > 14:
        imposible = True # no puede tener más de 14 cubos azules
        break
  if not imposible:
    num_game = re.findall(r"Game (\d+)", cadena)
    suma += int(num_game[0])

print(suma)