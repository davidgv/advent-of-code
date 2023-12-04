import re

with open("day02-input.txt", "r") as archivo:
  lista_archivo = archivo.readlines()

suma = 0

for cadena in lista_archivo:
  game = re.findall(r"(\d+) (\w+)", cadena)
  posible = True

  for par in game:
    if (par[1] == "red") and (int(par[0]) > 12) :
        posible = False # no puede tener más de 12 cubos rojos
        break
    if (par[1] == "green") and (int(par[0]) > 13) :
        posible = False # no puede tener más de 13 cubos verdes
        break
    if (par[1] == "blue") and (int(par[0]) > 14) :
        posible = False # no puede tener más de 14 cubos azules
        break
    
  if posible:
    num_game = re.findall(r"Game (\d+)", cadena)
    suma += int(num_game[0])

print(suma)