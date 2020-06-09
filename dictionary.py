murid_murid = []
murid = {}
tries = 0


while tries != 3:
  a = input("Masukkan key: ")
  b = input("Masukkan value: ")

  murid[a] = b

  for key in murid.keys():
    print(key)
    if key == a:
      murid_next = {}
      murid_next[a] = b
      murid_murid.append(murid_next)
    else:
      murid[a]= b
  tries += 1

print(murid_murid)
