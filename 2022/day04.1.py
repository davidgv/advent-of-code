with open("D:\\dev\\advent-of-code\\2022\\day04-input.txt", "r") as archivo:

  lista_parejas = archivo.readlines()
  cuantos_contienen = 0 # Cuantas asignaciones contienen a su pareja

  for pareja in lista_parejas:

    pareja = pareja.rstrip("\n")
    asig_pareja = pareja.rsplit(",")
    asigna1 = asig_pareja[0].rsplit("-")
    asigna2 = asig_pareja[1].rsplit("-")
    for i in range(2): # Convierte los valores de la lista en enteros
      asigna1[i] = int(asigna1[i])
      asigna2[i] = int(asigna2[i])
    contiene = False # Indica si uno contiene a otro

    if (asigna1[0] <= asigna2[0]) and (asigna1[1] >= asigna2[1]) : # asigna1 contiene asigna2 ??
      contiene = True
    elif (asigna2[0] <= asigna1[0]) and (asigna2[1] >= asigna1[1]) : # asigna2 contiene asigna1 ??
      contiene = True
    
    if contiene:
      cuantos_contienen += 1

print(cuantos_contienen)
