#arbitrary argument
def add(*x):
    print(x)
    total = 0
    if(len(x)==20):
       for i in x:
           total += i
    return total    
print(add(20))    