#User function Template for python3
class node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def createTree(self, root, l):
        # Code here
        if not l:
            return None
       
        # Initialize the root with the first element of the list
        root.data = l[0]
        # Initialize a queue with the root node
        queue = [root] 

        i = 1 # Start from 2nd element of the list
        while i < len(l): 
            current = queue.pop(0) # Get the current node from the queue
            
            # Assign the left child
            if i < len(l):
                current.left = node(l[i])
                queue.append(current.left)
                i += 1
                
            # Assign the right child
            if i < len(l):
                current.right = node(l[i])
                queue.append(current.right)
                i += 1
            
        return root
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

def traverseInorder(temp, inorder):
    if(temp!=None):
        traverseInorder(temp.left, inorder)
        inorder.append(temp.data)
        traverseInorder(temp.right, inorder)
    return
    
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        arr= list(map(int, input().split()))
        root=Node(arr[0])
        root.left=Node(arr[1])
        root.right=Node(arr[2])
        root.left.left=Node(arr[3])
        root.left.right=Node(arr[4])
        root.right.left=Node(arr[5])
        root.right.right=Node(arr[6])
        
        
        obj=Solution()
        root0=Node(arr[0])
        obj.createTree(root0, arr)
        
        a=[]
        traverseInorder(root0, a)
        b=[]
        traverseInorder(root, b)
        
        if(a==b):
            print(1)
        else:
            print(-1)
# } Driver Code Ends