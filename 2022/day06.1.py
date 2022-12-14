with open("D:\\dev\\advent-of-code\\2022\\day06-input.txt", "r") as archivo:
  paquete = archivo.readline()

ini_paq = 0 # Número de caracteres antes del primer "marcador de inicio de paquete"

for i in range(len(paquete)):
  c1_cuantos = paquete.count(paquete[i], i, i+4) # Num. apariciones carácter 1
  c2_cuantos = paquete.count(paquete[i+1], i, i+4) # Idem carácter 2
  c3_cuantos = paquete.count(paquete[i+2], i, i+4) # Idem carácter 3
  if (c1_cuantos == 1) and (c2_cuantos == 1) and (c3_cuantos == 1) :
    ini_paq = i+4
    break

print(ini_paq)
