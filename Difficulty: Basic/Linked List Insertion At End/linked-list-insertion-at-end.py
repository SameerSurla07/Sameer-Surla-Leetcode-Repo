'''    
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
'''
class Solution:
    #Function to insert a node at the end of the linked list.
    def insertAtEnd(self,head,x):
        # code here 
        # Create a new node with the given value x
        new_node = Node(x)
        
        # If the list is empty, return the new node as the head
        if head is None:
            return new_node

        # Traverse the list to find the last node
        current_node = head
        while current_node.next is not None:
            current_node = current_node.next
        
        # Set the next pointer of the last node to the new node
        current_node.next = new_node
        
        return head


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Define the Node class for the linked list
class Node:

    def __init__(self, x):
        self.data = x
        self.next = None


# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


#Position this line where user code will be pasted.

# Main function
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    idx = 1

    while t > 0:
        arr = list(map(int, data[idx].strip().split()))
        x = int(data[idx + 1].strip())
        idx += 2

        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for num in arr[1:]:
                tail.next = Node(num)
                tail = tail.next

        ob = Solution()
        ans = ob.insertAtEnd(head, x)
        printList(ans)

        t -= 1

# } Driver Code Ends