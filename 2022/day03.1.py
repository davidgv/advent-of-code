with open("D:\\dev\\advent-of-code\\2022\\day03-input.txt", "r") as archivo:
  mochilas = archivo.readlines()

prioridad_total = 0 # El dato buscado

for mochila in mochilas:

  mochila = mochila.rstrip() # Elimina el salto de línea de la cadena
  tam_compartimento = len(mochila) // 2
  flag_salir = False # Salir anticipadamente del doble bucle siguiente

  # Compara todos los artículos del primer compartimento con los del segundo, hasta encontrar el duplicado
  for i in range(tam_compartimento):
    if flag_salir:
      break
    for j in range(tam_compartimento, len(mochila), 1):
      if mochila[i] == mochila[j] :
        art_repetido = mochila[i]
        flag_salir = True
        break

  # Calcula prioridad del artículo repetido
  ascii_art_rep = ord(art_repetido)
  if (ascii_art_rep >= 97) and (ascii_art_rep <= 122) : # Intervalo a-z
    prioridad_art_rep = ascii_art_rep - 96
  if (ascii_art_rep >= 65) and (ascii_art_rep <= 90) : # Intervalo A-Z
    prioridad_art_rep = ascii_art_rep - 38
  
  prioridad_total += prioridad_art_rep

print(prioridad_total)
