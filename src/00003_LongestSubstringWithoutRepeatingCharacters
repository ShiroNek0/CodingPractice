from collections import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        
        chars = Counter()
        res = 0

        while (j < len(s)):
            r = s[j]
            chars[r] += 1

            while chars[r] > 1:
                chars[s[i]] -= 1
                i += 1

            res = max(res, j - i + 1)
            j += 1
            

        return res
