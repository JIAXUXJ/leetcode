# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    leftHeight = 0;
    rightHeight = 0;
    if (root.info is not None):
        if (root.left is not None):
            leftHeight = height(root.left) + 1
        if (root.right is not None):
            rightHeight = height(root.right) + 1
    
    return leftHeight if leftHeight > rightHeight else rightHeight