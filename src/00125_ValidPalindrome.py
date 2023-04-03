# https://leetcode.com/problems/valid-palindrome/submissions/927285775/

import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s= "".join(ch for ch in s if ch.isalnum())
        print(s)
        strLen = len(s)

        if strLen <= 1:
            return True

        i = 0
        j = strLen - 1

        while (i < j):
            if s[i] != s[j]:
                return False
            
            i += 1
            j -= 1

        return True
    