from pickle import APPEND


def calPoints(ops) -> int:
    result=0
    ops2=ops
    for j in range(len(ops)):        
        if (j==0 ):           
            if not (ops2[j].isnumeric()):
                print("Must be a number")
                break                                         
        else:                        
            if(ops2[j]=="C"):
                result-=int(ops2[j-1])
                result-=int(ops2[j-2])
                ops2.pop(j)
                ops2.pop(j-1)
                                
            elif(ops2[j]=="D"):                
                t=int(ops2[j]*2)                                             
                ops2.insert(j,t)
                ops2.pop(j) 
              
        print(ops2)
        print(ops)
    for i in range(len(ops)):
        result += int(ops2[i])
           
    return result

if __name__== '__main__':
    line = "5  4 C"
    ops = line.strip().split()    
    print(calPoints(ops))