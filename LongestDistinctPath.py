# Python3 program to find count of
# distinct nodes on a path with
# maximum distinct nodes.

# A utility class to create a
# new Binary Tree node
class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def largestUinquePathUtil(node, m):
if (not node):
return len(m)

# put this node into hash
if node.data in m:
m[node.data] += 1
else:
m[node.data] = 1

max_path = max(largestUinquePathUtil(node.left, m),
largestUinquePathUtil(node.right, m))

# remove current node from path “hash”
m[node.data] -= 1

# if we reached a condition
# where all duplicate value
# of current node is deleted
if (m[node.data] == 0):
del m[node.data]

return max_path

# A utility function to find
# long unique value path
def largestUinquePath(node):
if (not node):
return 0

# hash that store all node value
Hash = {}

# return max length unique value path
return largestUinquePathUtil(node, Hash)

# Driver Code
if __name__ == ‘__main__’:

# Create binary tree shown
# in above figure
root = newNode(1)
root.left = newNode(2)
root.right = newNode(3)
root.left.left = newNode(4)
root.left.right = newNode(5)
root.right.left = newNode(6)
root.right.right = newNode(7)
root.right.left.right = newNode(8)
root.right.right.right = newNode(9)

print(largestUinquePath(root))