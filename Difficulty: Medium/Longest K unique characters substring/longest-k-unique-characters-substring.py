#User function Template for python3

class Solution:

    def longestKSubstr(self, s, k):
        # code here
        from collections import defaultdict

        n = len(s)
        if n * k == 0:
            return 0
            
        # Sliding window left and right pointers
        left = 0
        right = 0

        # Hashmap to count the characters in the current window
        char_count = defaultdict(int)

        max_len = -1

        while right < n:
            # Add one character from the right to the window
            char_count[s[right]] += 1
            right += 1
            
            # Shrink the window until we have at most 'k' distinct characters
            while len(char_count) > k:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            if len(char_count) == k:
            # Update the maximum length of substring found
                max_len = max(max_len, right - left)
    
        return max_len 
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()
        k = int(input())

        solObj = Solution()

        ans = solObj.longestKSubstr(s, k)

        print(ans)

# } Driver Code Ends