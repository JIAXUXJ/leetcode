# Python 3 program to change value of 
# diagonal elements of a matrix to 0. 
MAX = 100

def print_1(mat, n, m): 
	
	for i in range(n): 
		for j in range(m): 
			print( mat[i][j], end = " ") 

		print() 

# function to change the values 
# of diagonal elements to 0 
def makediagonalzero(mat, n, m): 

	for i in range(n): 
		for j in range(m): 

			# right and left diagonal condition 
			if (i == j or (i + j + 1) == n): 
				mat[i][j] = 0

	# print resultant matrix 
	print_1(mat, n, m) 

# Driver code 
if __name__ == "__main__": 

	n = 3
	m = 3
	mat = [[ 2, 1, 7 ], 
		[ 3, 7, 2 ], 
		[ 5, 4, 9 ]] 

	makediagonalzero(mat, n, m) 

# This code is contributed by ChitraNayal 
