class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        half_len = len(s)//2
        for index in range(half_len):
            if s[index] != s[-(index + 1)]:        
                return False
        return True  
sol = Solution()
print(sol.isPalindrome(134443331))