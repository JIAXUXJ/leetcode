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

// Java program to change value of 
// diagonal elements of a matrix to 0. 
import java.io.*; 

class GFG { 
	public static void main (String[] args) { 
		int m[][] = {{ 2, 1, 7 }, 
					{ 3, 7, 2 }, 
					{ 5, 4, 9 }}; 
		int row = 3, col = 3; 
		GFG.diagonalMat(row,col,m); 
	} 
	// method to replace the diagonal matrix with zeros 
	public static void diagonalMat(int row, int col, int m[][]){ 
		
		// l is the left iterator which is 
		// iterationg from 0 to col-1[4] here 
		//k is the right iterator which is 
		// iterating from col-1 to 0 
		int i =0,l=0,k=col-1; 
		
		// i used to iterate over rows of the matrix 
		while(i<row){ 
			int j=0; 
			// condition to check if it is 
			// the centre of the matrix 
			if(l==k){ 
				m[l][k] = 0; 
				l++; 
				k--; 
			} 
			//otherwize the diagonal will be equivalaent to l or k 
			//increment l because l is traversing from left 
			//to right and decrement k for vice-cersa 
			else{ 
				m[i][l] = 0; 
				l++; 
				m[i][k]=0; 
				k--; 
			} 
			// print every element after replacing from the column 
			while(j<col){ 
				System.out.print(" "+ m[i][j]); 
				j++; 
			} 
			i++; 
			System.out.println(); 
		} 
		
	} 

} 

