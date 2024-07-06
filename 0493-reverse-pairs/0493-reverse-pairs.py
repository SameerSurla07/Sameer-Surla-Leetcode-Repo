from typing import List

class Solution:
    def merge(self, nums: List[int], temp: List[int], left: int, mid: int, right: int) -> int:
        # Count the number of reverse pairs
        j = mid + 1
        reverse_pairs_count = 0
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            reverse_pairs_count += j - (mid + 1)

        # Merge the two halves
        i = left
        j = mid + 1
        k = left
        while i <= mid and j <= right:
            if nums[i] <= nums[j]:
                temp[k] = nums[i]
                i += 1
            else:
                temp[k] = nums[j]
                j += 1
            k += 1

        while i <= mid:
            temp[k] = nums[i]
            i += 1
            k += 1

        while j <= right:
            temp[k] = nums[j]
            j += 1
            k += 1

        for i in range(left, right + 1):
            nums[i] = temp[i]

        return reverse_pairs_count

    def mergeSort(self, nums: List[int], temp: List[int], left: int, right: int) -> int:
        if left >= right:
            return 0

        mid = (left + right) // 2
        reverse_pairs_count = self.mergeSort(nums, temp, left, mid)
        reverse_pairs_count += self.mergeSort(nums, temp, mid + 1, right)
        reverse_pairs_count += self.merge(nums, temp, left, mid, right)

        return reverse_pairs_count

    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        temp = [0] * n
        return self.mergeSort(nums, temp, 0, n - 1)
