from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineHm = Counter(magazine)

        for c in ransomNote:
            if c in magazineHm:
                magazineHm[c] -= 1

                if magazineHm[c] < 0:
                    return False
            else:
                return False
        
        return True