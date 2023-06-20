from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def process(matrix, X, Y, startPosX, startPosY, result):
            if X < 1 or Y < 1:
                return

            for i in range(startPosY, startPosY+Y):
                result.append(matrix[startPosX][i])

            for i in range(startPosX+1, startPosX+X):
                result.append(matrix[i][startPosY+Y-1])

            if X > 1:
                for i in reversed(range(startPosY, startPosY+Y-1)):
                    result.append(matrix[startPosX+X-1][i])

                if Y > 1:
                    for i in reversed(range(startPosX+1, startPosX+X-1)):
                        result.append(matrix[i][startPosY])

            process(matrix, X-2, Y-2, startPosX+1, startPosY+1, result)

        R = len(matrix)
        C = len(matrix[0])
        result = []
        process(matrix, R, C, 0, 0, result)

        return result
