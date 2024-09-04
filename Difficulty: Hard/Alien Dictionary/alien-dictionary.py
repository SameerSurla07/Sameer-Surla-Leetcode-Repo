#User function Template for python3

from typing import List
from collections import defaultdict, deque

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Your implementation here

        # Kahn's ALgorithm
        
        # Step 1: Initialize a grpah and an in-degree array
        graph = defaultdict(list)
        in_degree = [0] * k
        
        # Step 2: Build the graph by comparing adjacent words in the dictionary
        for i in range(n-1):
            word1 = dict[i]
            word2 = dict[i+1]
            min_length = min(len(word1), len(word2))
            
            # find the first different character between the two words
            for j in range(min_length):
                if word1[j] != word2[j]:
                    # there is a directed edge from word1[j] to word2[j]
                    graph[ord(word1[j]) - ord('a')].append(ord(word2[j]) - ord('a'))
                    in_degree[ord(word2[j]) - ord('a')] += 1
                    break
                
        # Step 3: Initialize a queue and enqueue all characters with in-degree 0
        queue = deque()
        for i in range(k):
            if in_degree[i] == 0:
                queue.append(i)
            
        # Step 4: Perform topological sorting using Kahn's Algorithm
        topo_order = []
        while queue:
            current = queue.popleft()
            topo_order.append(current)
            
            # Decrease the in-degree of all neighbors of this current vertex
            for neighbor in graph[current]:
                in_degree[neighbor] -= 1
                # If in_degree of this neighbor becomes 0, add it to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                
        # Step 5: COnvert this topological order back to characters
        if len(topo_order) != k:
            return ''
        else:
            return "".join(chr(i + ord('a')) for i in topo_order)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


class sort_by_order:

    def __init__(self, s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i

    def transform(self, word):
        new_word = ''
        for c in word:
            new_word += chr(ord('a') + self.priority[c])
        return new_word

    def sort_this_list(self, lst):
        lst.sort(key=self.transform)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        line = input().strip().split()
        n = int(line[0])
        k = int(line[1])

        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob = Solution()
        order = ob.findOrder(alien_dict, n, k)
        s = ""
        for i in range(k):
            s += chr(97 + i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)

            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)

# } Driver Code Ends