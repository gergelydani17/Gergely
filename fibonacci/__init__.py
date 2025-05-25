x = int(input("szám: "))

fszamok = [0, 1]

i = 0
k = 2
#fibonacci számok feltöltése listába az input által megadott számig
while i <= x:
    fszamok.append(fszamok[k-1] + fszamok[k-2])
    k += 1
    i = fszamok[k-1]
#a 3-mal oszthatók kiválasztása és kiírása
j = 0
while j < len(fszamok):
    if fszamok[j] % 3 == 0:
        print(fszamok[j], end=", ")
    j += 1
