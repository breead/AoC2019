filepath = 'input'
place = 0
position1 = 0
position2 = 0
summa = 0
product = 0
noun = 0
verb = 0

opcodes = open(filepath,'r')
opcodelist = (opcodes.read()).split(',')
opcodelist = [int(i) for i in opcodelist]

while True:
    opcodes = open(filepath,'r')
    opcodelist = (opcodes.read()).split(',')
    opcodelist = [int(i) for i in opcodelist]
    #print("list before is:", *opcodelist)

    opcodelist[1] = noun
    #print("noun used is", opcodelist[1])
    opcodelist[2] = verb
    #print("verb used is", opcodelist[2])
    #print("list used is: ", *opcodelist)
    place = 0
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
    #print("list after is:", *opcodelist)
    #print("result is", opcodelist[0], "\n")
    if opcodelist[0] == 19690720:
        break
    elif opcodelist[1] < 99:
        noun += 1
        #print("noun is", noun)
        opcodes = open(filepath,'r')
        opcodelist = (opcodes.read()).split(',')
        opcodelist = [int(i) for i in opcodelist]
    elif verb < 99:
        noun = 0
        #print("verb is", verb)
        verb += 1
        opcodes = open(filepath,'r')
        opcodelist = (opcodes.read()).split(',')
        opcodelist = [int(i) for i in opcodelist]
    else:
        print("error, noun and verb are", noun, verb)
        break

print(str(opcodelist[place]), str(place), opcodelist[0], "answer should be:", 100 * noun + verb) #, "list:", *opcodelist)
