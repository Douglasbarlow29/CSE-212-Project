'''
This is an example problem where you will be creating a Binary Search Tree (BST)
and putting the values in order from smallest to greatest. There are two functions 
that you will use. The insert function will insert data into the tree based on it's 
value. The order function will then be used to put them in order. Finish the code 
in the marked areas to get the desired outcome.
'''

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.val = data


'''
This function will be used to insert a value into the tree
'''
def insert(root, data):
	if root is None:
		return Node(data))

	else:
        None

    #Write code in this else statement

	



'''
This function will put the numbers in order using recursion
'''
def order(root):
	if root:
        None

	#Write code in this if statement




tree = Node(6)
tree = insert(tree, 5)
tree = insert(tree, 2)
tree = insert(tree, 7)
tree = insert(tree, 3)
tree = insert(tree, 8)


order(tree) #Answer: 2, 3, 5, 6, 7, 8 