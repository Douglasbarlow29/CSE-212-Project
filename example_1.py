

def numbers(x):
    
    if x == 0:
        print(x)
    else:
        numbers(x-1)


numbers(5)