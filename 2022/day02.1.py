with open("D:\\dev\\advent-of-code\\2022\\day02-input.txt", "r") as archivo:
  lineas = archivo.readlines()

puntos_totales = 0 # Puntos totales de todas las rondas jugadas

for linea in lineas:

  mano1 = linea[0]
  mano2 = linea[2]

  # Puntos en función de ganar/empatar/perder
  if (mano2=="X" and mano1=="A") or (mano2=="Y" and mano1=="B") or (mano2=="Z" and mano1=="C"): # Empate
    puntos_ronda = 3
  elif (mano2=="X" and mano1=="C") or (mano2=="Y" and mano1=="A") or (mano2=="Z" and mano1=="B"): # Gana la ronda
    puntos_ronda = 6
  else: # Pierde la ronda
    puntos_ronda = 0

  # Puntos en función de la forma elegida
  if mano2 == "X": # Piedra
    puntos_forma = 1
  elif mano2 == "Y": # Papel
    puntos_forma = 2
  elif mano2 == "Z": # Tijeras
    puntos_forma = 3

  puntos_totales += (puntos_ronda + puntos_forma)

print(puntos_totales)
