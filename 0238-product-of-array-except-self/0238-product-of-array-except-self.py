class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                 
        n = len(nums)
        left = [1] * n
        right = [1] * n
        answer = [1] * n

        # Left array
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # Right array
        for i in range(n-2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        # Final result
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer























        # def from_to(from_ind, to):
        #     ans = 1
        #     for i in range(from_ind, to + 1):
        #         ans *= nums[i]
        #     return ans
       
       
        # n = len(nums)
        
        # result = []
        # # result.append(from_to(1, n - 1))

        # for i in range(n):
        #     result.append(from_to(0, i-1) * from_to(i + 1, n - 1))
       
        # return result