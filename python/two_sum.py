from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            hash1 = {}
            for index, num in enumerate(nums):
                complement = target - num
                if complement in hash1:
                    return [index, hash1[complement]]
                hash1[num] = index

sol = Solution()
print(sol.twoSum([2,7,11,15], 9))