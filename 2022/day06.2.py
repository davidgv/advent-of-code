with open("D:\\dev\\advent-of-code\\2022\\day06-input.txt", "r") as archivo:
  paquete = archivo.readline()

ini_men = 0 # Número de caracteres antes del primer "marcador de inicio de mensaje"

def se_repite(cadena):
# Se repite algun caracter en la "cadena" ??
  for i in range(14):
    if cadena.count(cadena[i]) > 1 :
      return True
  return False

for i in range(len(paquete)):
  if not se_repite(paquete[i:i+14]): # Lo encontramos !!
    ini_men = i+14
    break

print(ini_men)
