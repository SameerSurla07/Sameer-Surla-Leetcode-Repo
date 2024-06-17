class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False

        if c == 0:
            return True 

        for i in range(int(math.sqrt(c)) + 1):
            j = c - i*i
            if int(j**(0.5))**2 == j:
                return True
        return False