#User function Template for python3

'''

class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''

class Solution:
    # Function to reverse the linked list
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        return prev

    def addOne(self, head):
        # Step 1: Reverse the linked list
        head = self.reverse(head)

        # Step 2: Add 1 to the reversed list
        current = head
        carry = 1
        
        while current:
            new_value = current.data + carry
            carry = new_value // 10  # Determine if there is a carry
            current.data = new_value % 10  # Update the node's value
            
            # If there is no carry, break early to avoid unnecessary operations
            if carry == 0:
                break
            
            # Move to the next node
            if current.next is None and carry:
                # If we are at the end and still have a carry, add a new node
                current.next = Node(carry)
                carry = 0  # Set carry to 0 as we handled it
            current = current.next
        
        # Step 3: Reverse the list back to original order
        return self.reverse(head)

    
    
    
    
    
    
    
        # num_str = ""
        
        # current = head
        
        # while current is not None:
        #     num_str += str(current.data)
        #     current = current.next
        
        # num = int(num_str)
        # num += 1
        
        # num_str = str(num)
        
        # dummy = Node(0)
        # current = dummy
        
        # for digit in num_str:  # Convert the number to string and iterate over digits
        #     current.next = Node(int(digit))
        #     current = current.next

        # return dummy.next  # Return the next node after the dummy, which is the actual head

            
        
        
        
        
        
        
        
        
        
        
        
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Node Class
class Node:

    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            self.tail = self.head
        else:
            self.tail.next = Node(value)
            self.tail = self.tail.next
        self.size += 1


def PrintList(head):
    while head:
        print(head.data, end='')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        list1 = LinkedList()
        arr = list(map(int, input().strip().split()))
        first = arr[0]
        for i in arr:
            list1.insert(i)
        n1 = list1.size
        resHead = Solution().addOne(list1.head)

        n2 = 0
        current = resHead
        while current is not None:
            current = current.next
            n2 += 1
        if n2 == 1:
            if n1 > 1:
                print("Return the modified linkedlist")
            if n1 == 1:
                if first < 9:
                    PrintList(resHead)
                    print()
                else:
                    print("Return the modified linkedlist")
        else:
            PrintList(resHead)
            print()

# } Driver Code Ends