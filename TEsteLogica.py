lista = [34, 23, 56, 93, 10, 72]
while (len(lista) > 0):
  lista.pop()
  print(len(lista))
  if (len(lista) % 2 == 0 and len(lista) > 0):
    lista.pop()

