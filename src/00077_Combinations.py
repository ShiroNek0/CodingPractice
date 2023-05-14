from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(initNum: int, lst: List):
            if len(lst) == k:
                result.append(lst.copy())
                return
                    
            for i in range(initNum, n+1):
                lst.append(i)
                backtrack(i+1, lst)
                lst.pop()

        result = []
        backtrack(1, [])

        return result
