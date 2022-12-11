with open("D:\\dev\\advent-of-code\\2022\\day05-input.txt") as archivo:
  lineas_arch = archivo.readlines()

# Extraer las pilas del archivo de texto
pilas = [[],[],[],[],[],[],[],[],[]]
for fil in range(7,-1,-1):
  linea = lineas_arch[fil]
  for col in range(9):
    index_col = col*4+1 # Posición de la caja en el fichero txt
    if linea[index_col] != " " :
      pilas[col].insert(0, linea[index_col])

# Calculamos lista de movimientos
movimientos = []
for linea in lineas_arch:
  if linea.rfind("move") == 0 :
    desglose_linea = linea.rstrip("\n").split(" ")
    instrucciones = []
    instrucciones.append(desglose_linea[1])
    instrucciones.append(desglose_linea[3])
    instrucciones.append(desglose_linea[5])
    movimientos.append(instrucciones)

# Ejecutamos movimientos
for movimiento in movimientos:
  cuantos_mover = int(movimiento[0])
  mover_de = int(movimiento[1])
  mover_a = int(movimiento[2])
  for i in range(cuantos_mover):
    pilas[mover_a -1].insert(0, pilas[mover_de -1][0]) # Poner en destino
    pilas[mover_de -1].pop(0) # Eliminar origen

# Obtenemos el dato que buscamos
cajas_superiores = ""
for pila in pilas:
  cajas_superiores += pila[0]
print(cajas_superiores)
