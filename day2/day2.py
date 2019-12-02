filepath = 'input'
place = 0
position1 = 0
position2 = 0
summa = 0
product = 0

opcodes = open(filepath,'r')
opcodelist = (opcodes.read()).split(',')
opcodelist = [int(i) for i in opcodelist]

opcodelist[1] = 12
opcodelist[2] = 2

while True:
    if opcodelist[place] == 1:
        position1 = opcodelist[place + 1]
        position2 = opcodelist[place + 2]
        summa = opcodelist[position1] + opcodelist[position2]
        opcodelist[opcodelist[place + 3]] = summa
        place += 4
    elif opcodelist[place] == 2:
        position1 = opcodelist[place + 1]
        position2 = opcodelist[place + 2]
        product = opcodelist[position1] * opcodelist[position2]
        opcodelist[opcodelist[place + 3]] = product
        place += 4
    elif opcodelist[place] == 99:
        break
    else:
        print("error unknown opcode", opcodelist[place], "at", place)
        break
print(str(opcodelist[place]), str(place), opcodelist[0], "list:", *opcodelist)
