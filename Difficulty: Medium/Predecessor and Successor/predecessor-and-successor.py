'''
class Node:t
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
'''

class Solution:
    def __init__(self):
        self.pre = None
        self.suc = None

    def findPreSuc(self, root, pre, suc, key):
        # Start the search with the root
        self.helper(root, key)
        
        # Update pre and suc to the found predecessor and successor
        if self.pre:
            pre.key = self.pre.key
        if self.suc:
            suc.key = self.suc.key

    def helper(self, root, key):
        if not root:
            return
        
        # If the key is found
        if root.key == key:
            # The maximum value in the left subtree is the predecessor
            if root.left:
                temp = root.left
                while temp.right:
                    temp = temp.right
                self.pre = temp

            # The minimum value in the right subtree is the successor
            if root.right:
                temp = root.right
                while temp.left:
                    temp = temp.left
                self.suc = temp

        # If the key is smaller than the root's key, go to the left subtree
        elif key < root.key:
            self.suc = root  # This node could be the successor
            self.helper(root.left, key)

        # If the key is greater than the root's key, go to the right subtree
        else:
            self.pre = root  # This node could be the predecessor
            self.helper(root.right, key)

#{ 
 # Driver Code Starts

import queue

# BST Node
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def buildTree(ip):
    # Corner Case
    if len(ip) == 0 or ip[0] == 'N':
        return None

    # Create the root of the tree
    root = Node(int(ip[0]))

    # Push the root to the queue
    q = queue.Queue()
    q.put(root)

    # Starting from the second element
    i = 1
    while not q.empty() and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.get()

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))

            # Push it to the queue
            q.put(currNode.left)

        # For the right child
        i += 1
        if i >= len(ip):
            break
        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))

            # Push it to the queue
            q.put(currNode.right)

        i += 1

    return root


# Driver program to test above functions
t = int(input())
for _ in range(t):
    s = input()
    root = buildTree(s.split())
    k = int(input())
    pre = Node(None)
    succ = Node(None)
    ob = Solution()
    ob.findPreSuc(root, pre, succ, k)
    if pre.key:
        print(pre.key, end=' ')
    else:
        print(-1, end=' ')
    if succ.key:
        print(succ.key, end=' ')
    else:
        print(-1, end=' ')
    print()

# } Driver Code Ends