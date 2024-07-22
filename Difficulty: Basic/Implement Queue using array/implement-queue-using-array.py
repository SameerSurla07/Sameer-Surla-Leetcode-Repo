class MyQueue:
    def __init__(self, max_size=100000):
        self.max_size = max_size
        self.queue = [0] * self.max_size
        self.start = 0
        self.end = 0
        self.curr_size = 0

    # Function to push an element x into the queue
    def push(self, x):
        if self.curr_size == self.max_size:
            return "Queue is full"
        
        self.queue[self.end] = x
        self.end = (self.end + 1) % self.max_size
        self.curr_size += 1

    # Function to pop an element from the queue and return that element
    def pop(self):
        if self.curr_size == 0:
            return -1
        
        popped_element = self.queue[self.start]
        self.start = (self.start + 1) % self.max_size
        self.curr_size -= 1
        return popped_element

# Function to process a list of queries on the queue
def process_queries(queries):
    q = MyQueue()
    results = []
    
    for query in queries:
        if query[0] == 1:
            # Push operation
            q.push(query[1])
        elif query[0] == 2:
            # Pop operation
            results.append(q.pop())
    
    return results
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        s=MyQueue()
        q=int(input())
        q1=list(map(int,input().split()))
        i=0
        while(i<len(q1)):
            if(q1[i]==1):
                s.push(q1[i+1])
                i=i+2
            elif(q1[i]==2):
                print(s.pop(),end=" ")
                i=i+1
            elif(s.isEmpty()):
                print(-1)
                i=i+1
        print()   

# } Driver Code Ends