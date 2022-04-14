 
#Function to left Rotate arr[] of size n by 1*/
def leftRotatebyOne(arr, n):    
    for i in range(0,n):
        temp = arr[0]
        for j in range (0,len(arr)-1):
            arr[j] = arr[j+1]
        arr[len(arr)-1] = temp
         
def rightRotatebyOne(arr, n):
    for i in range(0, n):    
        last = arr[len(arr)-1];            
        for j in range(len(arr)-1, -1, -1):                  
            arr[j] = arr[j-1];          
        arr[0] = last
 
  
# Driver program to test above functions */

arr = [1, 2, 3, 4, 5, 6, 7]
print(arr)
#rightRotatebyOne(arr, 2)
print()
leftRotatebyOne(arr, 2)
print(arr)