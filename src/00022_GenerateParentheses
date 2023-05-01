# backtrack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(left:int, right:int, S):
            if len(S) == n*2:
                return result.append(S)

            if left < n:
                generate(left+1, right, S + "(")
            
            if right < left:
                generate(left, right+1, S + ")")

            return
        
        result =[]
        generate(0, 0, "")

        return result
