filepath = 'input'
def truncate(n, decimals=0):
     multiplier = 10 ** decimals
     return int(n * multiplier) / multiplier

with open(filepath) as ins:
    mass = 0
    total = 0
    for line in ins:
        mass = int(line)
        fuel = (truncate(mass/3))-2
        total += fuel
    print("the total amount of fuel needed is", total)

