#User function Template for python3
class Solution:
    def largestBst(self, root):
        # Your code here
        
        # Minimum Value, Maximum Value, Subtree Size, Is BST
        
        def postorder(node):
            if not node:
                return (float('inf'), float('-inf'), 0, True)
                
            # Recur for left and right subtrees
            left_min, left_max, left_size, left_is_bst = postorder(node.left)
            right_min, right_max, right_size, right_is_bst = postorder(node.right)

            # Check if the current subtree is a BST
            if left_is_bst and right_is_bst and left_max < node.data < right_min:
                # Current tree is a valid BST
                current_min = min(left_min, node.data)
                current_max = max(right_max, node.data)
                current_size = left_size + right_size + 1
                return ( current_min, current_max, current_size, True)
                
            else:
                # Current subtree is not a BST
                return (0, 0, max(left_size, right_size), False)
            
        # The third value in the tuple is the size of the largest BST subtree
        return postorder(root)[2]

























#{ 
 # Driver Code Starts
from collections import deque


# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None


# Function to Build Tree
def buildTree(s):
    # Corner Case
    if len(s) == 0 or s[0] == "N":
        return None

    # Creating list of strings from input string after splitting by space
    ip = list(map(str, s.split()))

    # Create the root of the tree
    root = Node(int(ip[0]))
    size = 0
    q = deque()

    # Push the root to the queue
    q.append(root)
    size += 1

    # Starting from the second element
    i = 1
    while size > 0 and i < len(ip):
        # Get and remove the front of the queue
        currNode = q.popleft()
        size -= 1

        # Get the current node's value from the string
        currVal = ip[i]

        # If the left child is not null
        if currVal != "N":
            # Create the left child for the current node
            currNode.left = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.left)
            size += 1

        # Move to the next element
        i += 1
        if i >= len(ip):
            break

        currVal = ip[i]

        # If the right child is not null
        if currVal != "N":
            # Create the right child for the current node
            currNode.right = Node(int(currVal))
            # Push it to the queue
            q.append(currNode.right)
            size += 1

        # Move to the next element
        i += 1

    return root


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        s = input()
        root = buildTree(s)
        ob = Solution()
        result = ob.largestBst(root)
        print(result)

# } Driver Code Ends