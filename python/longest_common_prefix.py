from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefixes = {}
        first_word = strs[0]
        if len(first_word) == 0:
            return ""
        actual_index = len(first_word) - 1
        for letter_index in range(len(first_word)):
            prefixes[letter_index]= first_word[:letter_index + 1]
        for word in strs:
            if not word:
                return ""
            for letter_index in range(len(word)):
                if word[:letter_index + 1] not in prefixes.values() and letter_index - 1 <= actual_index:
                    actual_index = letter_index - 1
                    break
                if word[:letter_index + 1] in prefixes.values() and letter_index + 1  == len(word) and letter_index <= actual_index:
                    actual_index = letter_index
        print(actual_index, "actualindex")
        print(prefixes, "prefixes")
        return prefixes[actual_index]

sol = Solution()
print(sol.longestCommonPrefix(["abab","aba",""]))