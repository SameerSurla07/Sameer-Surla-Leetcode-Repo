class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        child = 0     # Will run through greed factor
        cookie = 0   # Will run through cookie sizes

        g.sort()
        s.sort()

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                child += 1    
            cookie += 1

        return child
