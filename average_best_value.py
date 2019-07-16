
import random
from math import sqrt

def roll(diesize:int)->int:
    return random.randint (1,diesize)

def avg_roll(diesize:int=6, ntries:int =2)-> float: 
    ''' give average of several tries from rolling '''
    sum = 0.0
    for i in range(1, ntries):
        sum += roll(diesize)
    return float(sum/ntries)

def best_roll(diesize:int=6, ntries:int =2)-> float: 
    best = -1.0
    for i in range(0, ntries):
        current = roll(diesize)
        if current > best: best = current

    return best

def variance (mean:float, data:list):
    """ sum of the squares of the distance from the mean divided by number of data """ 
    sum = 0.0 
    for d in data:
        sum += (mean - d)**2 
    return sqrt(sum/len(data))

def mcarlo_best_roll (diesize:int, ntries:int, ntests:int=10000)->str:

    data = []
    sum = 0
    for i in range(0, ntests): 
        result = best_roll(diesize, ntries)
        sum += result
        data.append(result)

    # calculate average best roll and variance
    average = float(sum/ntests)
    error = variance (average, data)

    return (f'''%s +/- %s''' % (average, error))

print ("average best rolls by trials")
for ntries in range(1,11):
    print (f''' * average best in %s tries %s ''' % (ntries, mcarlo_best_roll(100, ntries)))

