cont = 0

while True:
    print(cont)
    cont = cont + 1
    if cont%3 != 0:
        continue
    print (cont)
    if cont >20:
        break
    print(cont)