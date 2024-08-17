#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def printBoundaryView(self, root):
        # Code here
        if not root:
            return []
            
        def is_leaf(node):
            return (node.left is None and node.right is None)
        
        def add_left_boundary(node, result):
            while node:
                if not is_leaf(node):
                    result.append(node.data)
                if node.left:
                    node = node.left
                else:
                    node = node.right

        def add_leaves(node, result):
            if is_leaf(node):
                result.append(node.data)
            if node.left:
                add_leaves(node.left, result)
            if node.right:
                add_leaves(node.right, result)
            
        
        def add_right_boundary(node, result):
            temp = []
            while node:
                if not is_leaf(node):
                    temp.append(node.data)
                if node.right:
                    node = node.right
                else:
                    node = node.left

            # Add right boundary in reverse order
            result.extend(temp[::-1])
        
        result = []
        
        # Add the root node if it's not a leaf node
        if not is_leaf(root):
            result.append(root.data)
        
        # Step 1: Add left boundary nodes (excluding leaf nodes)
        add_left_boundary(root.left, result)
        
        # Step 2: Add leaf nodes
        add_leaves(root, result)
        
        # Step 3: Add right boundary nodes (in reverse order and excluding leaf nodes)
        add_right_boundary(root.right, result)
        
        return result

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

# function should return a list containing the boundary view of the binary tree
#{ 
#  Driver Code Starts
import sys

import sys
sys.setrecursionlimit(100000)
#Contributed by Sudarshan Sharma
from collections import deque
# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root
    
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        obj = Solution()
        res = obj.printBoundaryView(root)
        for i in res:
            print (i, end = " ")
        print('')
# } Driver Code Ends