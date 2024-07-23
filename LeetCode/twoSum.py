from typing import List

class Solution(object):
    def twoSum(self, nums, target:int) -> int:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        size: int = len(nums)
        double_array = [[None for _ in range(size)] for _ in range(size )]
        for i in range(size-1):
            for j in range(1 + i, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
        

            

t = Solution()
t.twoSum( nums=[9, 5, 6, 1, 2], target=3)