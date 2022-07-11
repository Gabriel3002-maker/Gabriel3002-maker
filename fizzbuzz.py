for x in range(1,100):
    divisiblebythree = x % 3 == 0
    divisiblebyfive = x % 5 == 0
    
    if divisiblebythree and divisiblebythree:
        print('fizzbuzz')
    elif divisiblebythree:
        print('fizz')
    elif(divisiblebyfive):
        print('buzz')
    else:
        print(x)