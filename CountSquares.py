# Write a function that gets the number of squares between two numbers  
#method 1
def CountSquares(a, b): 
  
    cnt = 0 # initialize result 
  
    # Traverse through all numbers 
    for i in range (a, b + 1): 
        j = 1; 
        while j * j <= i: 
            if j * j == i: 
                 cnt = cnt + 1
            j = j + 1
        i = i + 1
    return cnt 

 # method2
 # An Efficient Method to count squares between a 
# and b 
import math 
def CountSquares(a, b): 
    return (math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1) 
  
# Driver Code 
a = 9
b = 25
print "Count of squares is:", int(CountSquares(a, b)) 