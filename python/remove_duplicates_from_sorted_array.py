from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        pop = []
        for index, num in enumerate(nums):
            if num in seen:
                pop.append(index)
            seen.add(num)
        for index in reversed(pop):
            nums.pop(index)
        return len(nums)
sol = Solution()
print(sol.removeDuplicates([1,2,2,2,2,2,3,3])) 