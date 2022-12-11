with open("D:\\dev\\advent-of-code\\2022\\day02-input.txt", "r") as archivo:
  lineas = archivo.readlines()

puntos_totales = 0 # Puntos totales de todas las rondas jugadas

for linea in lineas:

  mano1 = linea[0]
  resul_ronda = linea[2]

  # Calculamos mano2 en función de mano1 y resul_ronda
  if (mano1=="B" and resul_ronda=="X") or (mano1=="A" and resul_ronda=="Y") or (mano1=="C" and resul_ronda=="Z"): # Piedra
    mano2 = "X"
  elif (mano1=="C" and resul_ronda=="X") or (mano1=="B" and resul_ronda=="Y") or (mano1=="A" and resul_ronda=="Z"): # Papel
    mano2 = "Y"
  else: # Tijeras
    mano2 = "Z"

  # Puntos en función de ganar/empatar/perder
  if resul_ronda == "X": # Perder
    puntos_ronda = 0
  elif resul_ronda == "Y": # Empatar
    puntos_ronda = 3
  else: # Ganar
    puntos_ronda = 6

  # Puntos en función de la forma elegida
  if mano2 == "X": # Piedra
    puntos_forma = 1
  elif mano2 == "Y": # Papel
    puntos_forma = 2
  elif mano2 == "Z": # Tijeras
    puntos_forma = 3

  puntos_totales += (puntos_ronda + puntos_forma)

print(puntos_totales)
