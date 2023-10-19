import math

modules = []
total = fuel = 0

with open('input.txt', 'r') as f: #reading file
    modules = f.read().splitlines() #copy lines to array 1st = 19115 2nd = 49739
    #print(modules)
        
    for x in modules:
        mass = int(x)
        fuel = (math.floor(mass/3))-2
        total = fuel +total
    print(total)
    #calculate every module
    

deneme2'de değişiklik
