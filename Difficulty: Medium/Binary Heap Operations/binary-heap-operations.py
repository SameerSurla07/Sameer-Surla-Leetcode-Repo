#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''

curr_size = 0  # No elements in the heap initially

# Helper function to get the parent index of node x
def getParent(x):  
    return (x - 1) // 2  # Returns the parent index or -1 if it's the root

# Helper function to get the left child index of node x
def leftChild(x):  
    return (2 * x + 1) if (2 * x + 1) < curr_size else -1  # Returns left child index or -1 if it doesn't exist

# Helper function to get the right child index of node x
def rightChild(x):  
    return (2 * x + 2) if (2 * x + 2) < curr_size else -1  # Returns right child index or -1 if it doesn't exist

# Function to maintain the min-heap property by moving the node upwards
def heapify():
    # Start with the last inserted node
    curr_ind = curr_size - 1
    
    # Move the node upwards until the heap property is restored
    while getParent(curr_ind) != -1 and heap[getParent(curr_ind)] > heap[curr_ind]:
        # Swap the node with its parent if the parent is larger
        heap[curr_ind], heap[getParent(curr_ind)] = heap[getParent(curr_ind)], heap[curr_ind]
        curr_ind = getParent(curr_ind)  # Update the current index to the parent
    
    return

# Function to maintain the min-heap property by moving the node downwards
def heapifyDown(x):
    if x >= curr_size:  # If the node is a leaf, nothing to do
        return
    
    # If the current node is smaller than its parent, swap with parent
    if getParent(x) != -1 and heap[x] < heap[getParent(x)]:
        heap[x], heap[getParent(x)] = heap[getParent(x)], heap[x]
        heapifyDown(getParent(x))  # Recursively heapify upwards
    
    # If both children exist, ensure that the smaller child is swapped
    if leftChild(x) != -1 and (heap[x] > heap[leftChild(x)] or (rightChild(x) != -1 and heap[x] > heap[rightChild(x)])):
        
        if rightChild(x) == -1:  # If only the left child exists
            heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
            heapifyDown(leftChild(x))
        
        elif leftChild(x) == -1:  # If only the right child exists
            heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
            heapifyDown(rightChild(x))
        
        else:  # Both children exist, swap with the smaller child
            if heap[rightChild(x)] < heap[leftChild(x)]:
                heap[x], heap[rightChild(x)] = heap[rightChild(x)], heap[x]
                heapifyDown(rightChild(x))
            else:
                heap[x], heap[leftChild(x)] = heap[leftChild(x)], heap[x]
                heapifyDown(leftChild(x))
    return

# Function to insert a value into the heap
def insertKey(x):
    global curr_size
    
    # Insert the new value at the current available position
    heap[curr_size] = x
    curr_size += 1
    
    # Restore the heap property after insertion
    heapify()

# Function to delete a key at index i
def deleteKey(i):
    global curr_size
    
    if i >= curr_size:  # If the index is invalid
        return
    
    # Replace the element at index i with the last element in the heap
    heap[i] = heap[curr_size - 1]
    heap[curr_size - 1] = 0  # Clear the last position
    curr_size -= 1  # Decrease the size of the heap
    
    # Restore the heap property after deletion
    heapifyDown(i)

# Function to extract the minimum element from the heap
def extractMin():
    if curr_size == 0:  # If the heap is empty
        return -1
    
    # The minimum element is the root of the heap
    val = heap[0]
    
    # Remove the root and restore the heap property
    deleteKey(0)
    
    return val

    



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends