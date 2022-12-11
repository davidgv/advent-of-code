with open("d:\dev\\advent-of-code\\2022\\day01-input.txt", "r") as archivo:
  lineas = archivo.readlines()

valor_tmp = 0
valor_max = 0
for linea in lineas:
  if linea == "\n":
    valor_tmp = 0
  else:
    valor_tmp += int(linea)
    if valor_tmp > valor_max:
      valor_max = valor_tmp

print(valor_max)
