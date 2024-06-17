class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0:
            return False

        if c == 0:
            return True 
        start = 0
        end = int(math.sqrt(c))

        while start <= end:
            current_sum = start * start + end * end
            if current_sum == c:
                return True
            elif current_sum > c:
                end -= 1
            else:
                start += 1


        return False
        # for i in range(int(math.sqrt(c)) + 1):
        #     j = c - i*i
        #     if int(j**(0.5))**2 == j:
        #         return True
        # return False