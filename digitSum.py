# Python 3 program to 
# compute sum of digits in  
# number. 
  
# Function to get sum of digits  
def getSum(n): 
   
    sum = 0
    while (n != 0): 
      
        sum = sum + int(n % 10) 
        n = int(n/10) 
      
    return sum
  
n = 687
print(getSum(n)) 