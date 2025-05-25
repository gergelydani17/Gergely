min = int(input("min: "))
max = int(input("max: "))

ivallum = abs(max - min + 1)
dobokockak = [20, 10, 8, 6, 4, 3, 2]
eredmeny = [0, 0, 0, 0, 0, 0, 0]

i = 0
while i < len(dobokockak):
    if ivallum % dobokockak[i] == 1:
        i += 1
    eredmeny[i] += ivallum // dobokockak[i]
    ivallum -= dobokockak[i] * eredmeny[i]
    i += 1

j = 0
for k in range(len(eredmeny)):
    if eredmeny[k] != 0:
        if j != 0:
            print("+", end="")
        print(eredmeny[k], "d", dobokockak[k], sep="", end="")
        j += 1

if min > 1:
    print("+", end="")
if min != 1:
    print(min-1)
