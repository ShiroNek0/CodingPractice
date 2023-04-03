## 242. Valid Anagram
## https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        for char in s:
            if char in sDict:
                sDict[char] += 1
            else:
                sDict[char] = 1

        tDict = {}
        for char in t:
            if char in tDict:
                tDict[char] += 1
            else:
                tDict[char] = 1

        if len(sDict) != len(tDict):
            return False

        for key in sDict:
            if key in tDict:
                if sDict[key] == tDict[key]:
                    continue
            return False

        return True


