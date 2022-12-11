with open("D:\\dev\\advent-of-code\\2022\\day03-input.txt", "r") as archivo:
  mochilas = archivo.readlines()

prioridad_total = 0 # El dato buscado

for grupo in range(0, len(mochilas), 3):

  mochila1 = mochilas[grupo].rstrip()
  mochila2 = mochilas[grupo+1].rstrip()
  mochila3 = mochilas[grupo+2].rstrip()
  flag_salir = False # Salir anticipadamente de la búsqueda siguiente

  # Busca el elemento común en las 3 mochilas
  for elemento1 in mochila1:
    if flag_salir:
        break
    for elemento2 in mochila2:
      if flag_salir:
        break
      for elemento3 in mochila3:
        if elemento1 == elemento2 == elemento3 :
          flag_salir = True
          break

  # Calcula prioridad del elemento común
  ascii_ele_comun = ord(elemento3)
  if (ascii_ele_comun >= 97) and (ascii_ele_comun <= 122) : # Intervalo a-z
    prioridad_ele_comun = ascii_ele_comun - 96
  if (ascii_ele_comun >= 65) and (ascii_ele_comun <= 90) : # Intervalo A-Z
    prioridad_ele_comun = ascii_ele_comun - 38
  
  prioridad_total += prioridad_ele_comun

print(prioridad_total)
