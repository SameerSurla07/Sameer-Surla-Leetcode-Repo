# function should return parent of x
def find(arr, x):
    if arr[x-1]==x:
        return x
    arr[x-1]=find(arr,arr[x-1])
    return arr[x-1]
# function shouldn't return or print anything
def unionSet(arr, x, z):
    arr[find(arr,x)-1]=find(arr,z)



#{ 
 # Driver Code Starts
if __name__=='__main__':
    T = int(input())
    for _ in range(T):
        n,k = list(map(int, input().strip().split()))
        arr = [x for x in range(1, n+1)]
        s = input().strip().split()
        i = 0
        while i<len(s):
            if s[i]=='FIND':
                print(find(arr, int(s[i+1])), end=" ")
                i+=2
            elif s[i]=='UNION':
                unionSet(arr, int(s[i+1]), int(s[i+2]))
                i+=3
        print()
# Contributed by: Harshit Sidhwa

# } Driver Code Ends