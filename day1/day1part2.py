filepath = 'input'
def truncate(n, decimals=0):
     multiplier = 10 ** decimals
     return int(n * multiplier) / multiplier

with open(filepath) as ins: 
    mass = 0
    fuelmass = 0
    total = 0
    def getmass(m):
        return truncate(m/3)-2 
    for line in ins:
        mass = int(line)
        fuel = (truncate(mass/3))-2
        print("fuel is equal to", fuel)
        fuelmass = getmass(fuel)
        print("fuelmass is equal to", fuelmass)
        totalfuelmass = 0
        while(fuelmass >= 0):
            totalfuelmass += fuelmass
            fuelmass = getmass(fuelmass)
            print("totalfuelmass is equal to", totalfuelmass)
        total += fuel + totalfuelmass
    print("the total amount of mass needed is", total)

