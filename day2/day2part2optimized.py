#My solution to part two of the second day's problem from Advent of Code 2019
#Define some vars
filepath = 'input'
place = 0
position1 = 0
position2 = 0
summa = 0
product = 0
noun = 0
verb = 0

while True:
    #Set/reset the input intcode list
    opcodes = open(filepath,'r')
    opcodelist = (opcodes.read()).split(',')
    opcodelist = [int(i) for i in opcodelist]

    #Set the noun and verb (position 1 and 2) to the values of the variables set last loop run
    opcodelist[1] = noun
    opcodelist[2] = verb
    place = 0
    #Loop that runs the intcode
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
    #Check if the output item in the list at position 0 has a satisfactory value
    if opcodelist[0] == 19690720:
        break
    #If not, increment the noun value by one. Do this until it hits 99, where it rolls over and the verb value is increased by one.
    #Then increment the verb value until it hits 99. If no satisfactory outcome is found, print an error
    elif opcodelist[1] < 99:
        noun += 1
    elif verb < 99:
        noun = 0
        verb += 1
    else:
        print("error, noun and verb are", noun, verb)
        break
#Print the answer in the format from the instructions
print("answer should be:", 100 * noun + verb)
