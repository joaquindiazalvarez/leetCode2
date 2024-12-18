from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        numbers = sorted(nums)
        for i in range (len(numbers)):
            hi, lo = len(nums) - 1, i + 1
            if i > 0 and numbers[i] == numbers[i-1]:
                continue
            if lo == len(numbers) - 1:
                break
            while lo < hi:
                total = numbers[i] + numbers[lo] + numbers[hi]
                if total == 0:
                    if numbers[i] + numbers[lo] + numbers[hi] == 0 and hi != lo:
                        
                        answer.append([numbers[i], numbers[lo], numbers[hi]])
                    while lo < hi and numbers[lo] == numbers[lo + 1]:
                        lo += 1
                    while lo < hi and numbers[hi] == numbers[hi - 1]:
                        hi -= 1
                    lo += 1
                    hi -= 1
                elif total < 0:
                    lo += 1
                else:
                    hi -= 1
        return answer
sol = Solution()
print(sol.threeSum([1,-1,-1,0]
))


