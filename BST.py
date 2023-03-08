import time
import random

# CCDSALG MCO2
# @author ANG, Elliamae
# @author MOJICA, John Marvic
# @author PALLASIGUE, Diego
# @author SILVESTRE, Franczeska

# Python program that implements BST

class Node:
    def __init__(self,val=None):
        self.left = None
        self.right = None
        self.val = val
        self.counter = 0
    def increment(self):
        self.counter += 1 

    # insert() – adds a new node in the BST
    def insert(self,val):
        if not self.val:
            self.val = val
            return

        if self.val == val:
            return

        if val < self.val:
            if self.left:
                self.left.insert(val)
                return
            self.left = Node(val)
            return

        if self.right:
            self.right.insert(val)
            return
        self.right = Node(val)

    # search() – determines if a search key exists in the BST
    def search(self,val):
        if val == self.val:     #node already in tree
            self.increment()
            return True

        if val < self.val:
            if self.left == None:   #traverse left, node not in tree
                return False
            return self.left.search(val)
        
        if self.right == None:      #traverse right, node not in tree
            return False   
        return self.right.search(val)

class BinarySearchTree:
    def __init__(self,node=None):
        self.root = node

    # create() – produces an empty BST
    def create(self, value):
        if self.root:   #if root exists
            self.root.insert(value)
        else:           #if no root yet
            self.root = Node(value)

    def search(self, value):
        if self.root:
            return self.root.search(value) #will return true if exists, false otherwise
        else:
            return False

# Print (for checking if logic is correct)
def printInorder(root):
 
    if root:
 
        # First recur on left child
        printInorder(root.left)
 
        # then print the data of node
        print(root.val),
 
        # now recur on right child
        printInorder(root.right)


# Get input
print("Binary Search Tree")
n = int(input("Enter string length (n): "))
k = int(input("Enter k value: "))

# Generate string with length n
str = "acgt"
seq = "".join((random.choice(str) for _ in range(n)))

# Make empty BST
tree = BinarySearchTree()

# Measure execution time
timeStart = time.time()

# Insert node into BST
for i in range(n-k+1):
    substr = seq[i:i+k]
    if tree.search(substr) is False:
        tree.create(substr)

# Measure execution time
timeEnd = time.time()

# TESTING: Call inorder traversal here (Comment out when testing large n)
# printInorder(tree.root)

# Print execution time
print("Total execution time (in seconds): ", timeEnd - timeStart)