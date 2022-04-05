'''
This is an example problem where you will be creating a Binary Search Tree (BST)
and putting the values in order from smallest to greatest. There are two functions 
that you will use. The insert function will insert data into the tree based on it's 
value. The order function will then be used to put them in order. Finish the code 
to get the desired outcome.
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
		return Node(data)
        #If the root node is empty then we insert the value
	else:
		if root.val == data:
			return root
            #Check to see if data is equal to the root node
		elif root.val < data:
			root.right = insert(root.right, data)
            #Check to see if the data is greater than root node
            #If it is then we insert it to the right of root node
		else:
			root.left = insert(root.left, data)
            #Check to see if the data is less than root node
            #If it is then we insert it to the left of root node
	return root



'''
This function will put the numbers in order using recursion
'''
def order(root):
	if root:

        #Recursion is used to get the correct values in the correct order
		order(root.left)
		print(root.val)
		order(root.right)



#Insert the numbers
tree = Node(6)
tree = insert(tree, 5)
tree = insert(tree, 2)
tree = insert(tree, 7)
tree = insert(tree, 3)
tree = insert(tree, 9)

#Put them in order
order(tree) #Answer: 2, 3, 5, 6, 7, 9 