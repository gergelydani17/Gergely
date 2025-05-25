x = int(input("szám: "))

fszamok = [0, 1]

i = 0
k = 2

while i <= x:
    fszamok.append(fszamok[k-1] + fszamok[k-2])
    k += 1
    i = fszamok[k-1]

j = 0
while j < len(fszamok):
    if fszamok[j] % 3 == 0:
        print(fszamok[j], end=", ")
    j += 1
