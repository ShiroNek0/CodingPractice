class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s= "".join(ch for ch in s if ch.isalnum())
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


# import math

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         s = s.lower()
#         s= "".join(ch for ch in s if ch.isalnum())
#         print(s)
#         strLen = len(s)

#         if strLen <= 1:
#             return True

#         middle = math.ceil(strLen/2) - 1
#         if strLen%2 == 0:
#             p1 = middle 
#             p2 = middle + 1
#         else:
#             p1 = middle - 1
#             p2 = middle + 1

#         for i in range(p2, strLen):
#             if s[p1] != s[p2]:
#                 return False
#             else:
#                 p1 -= 1
#                 p2 += 1

#         return True