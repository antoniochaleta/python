
# put your python code here
N = 1
lst=[]
odd=""
even=""
for i in range(1 , N+1, 1):
    lst.append(str(input()))
j=0
for word in lst:
    j=0
    even=""
    odd=""
    for i in word:        
        if j % 2 == 0:
            even += word[j]
        else:
            odd += word[j]
        j+=1
    print(even + " " + odd)


