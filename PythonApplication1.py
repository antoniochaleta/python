

def calPoints(ops) -> int:

    for x in ops:
        print(x)
    
    result = 50
    print(ops)
    return result

if __name__== '__main__':
    line = "5,2,C,D,+"
    ops = line.strip().split()    
    print(calPoints(ops))