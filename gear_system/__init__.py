target = input("kívánt állapot: ").replace("[","").replace("] ",", ").split(", ")









for i in range(len(target)):
    target[i] = int(target[i])

maxhuzasok = target[-1]
target.pop(target[-1])

left_lever = [1, 1, 0]
right_lever = [0, 1, 1]
indexer = [3, 1, 2, 3, 1, 2]
fogaskerekek = [3, 3, 3]

bh = 0
jh = 0
eredmeny = []






while bh + jh < 5:
    while fogaskerekek[0] != target[0]:
        for i in range(0, 2):
            if i == 1:
                fogaskerekek[i] = indexer[jh + bh + right_lever[i]]
            else:
                fogaskerekek[i] = indexer[bh + left_lever[i]]
        eredmeny.append("'left'")
        bh += 1
    if bh + jh >= maxhuzasok:
        break


    while fogaskerekek[1] != target[1]:
        for i in range(1, 3):
            if i == 1:
                fogaskerekek[i] = indexer[jh + bh + right_lever[i]]
            else:
                fogaskerekek[i] = indexer[jh + right_lever[i]]
        eredmeny.append("'right'")
        jh += 1
    if bh + jh > maxhuzasok:
        break
    



    if fogaskerekek == target:
        print(eredmeny)
        break
    if fogaskerekek[2] != target[2]:
        print("Megoldhatatlan")
        break





if fogaskerekek != target:
        print("Megoldhatatlan")
