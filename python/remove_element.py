class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for num in nums:
            if num != val:
                length += 1
        return length 