#User function Template for python3
'''
	Your task is to segregate the list of 
	0s,1s and 2s.
	
	Function Arguments: head of the original list.
	Return Type: head of the new list formed.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
class Solution:
    #Function to sort a linked list of 0s, 1s and 2s.
    def segregate(self, head):
        #code here
        
        if head is None or head.next is None:
            return head
            
        # Step 1: Count the occurrences of 0s, 1s, and 2s
        # Index 0 for 0s, index 1 for 1s, index 2 for 2s
        count = [0, 0, 0]

        current = head
        
        while current is not None:
            count[current.data] += 1
            current = current.next
            
        # Step 2: Modify list based on the counts
        current = head
        index = 0
        
        while current is not None:
            if count[index] == 0:
                index += 1
            else:
                current.data = index
                count[index] -= 1
                current = current.next
            
        return head
                
        
        
        
        
        
        
        
        
        
        
    


#{ 
 # Driver Code Starts
# Initial Template for Python 3


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        head = None
        if arr:
            head = Node(arr[0])
            tail = head
            for value in arr[1:]:
                tail.next = Node(value)
                tail = tail.next

        printList(Solution().segregate(head))

# } Driver Code Ends