with open("d:\dev\\advent-of-code\\2022\\day01-input.txt", "r") as archivo:

  lineas = archivo.readlines()
  elfos_cal = [] # aquí van las calorías totales por elfo
  suma_tmp = 0
  for linea in lineas:
    if linea == "\n":
      elfos_cal.append(suma_tmp)
      suma_tmp = 0
    else:
      suma_tmp += int(linea)
  
  elfos_cal.sort(reverse=True) # los 3 primeros valores de la lista son los 3 elfos con más calorías
  suma_cal = 0
  for i in range(3):
    suma_cal += elfos_cal[i]

print(suma_cal)
