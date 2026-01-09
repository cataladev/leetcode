class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        minVal = 10 ** 9 #makes it an int, 10e5 makes it a float
        negCount = 0
        absSum = 0
        for i in matrix:
            for j in i:
                absJ = abs(j)
                absSum += absJ
                if j < 0:
                     negCount = negCount + 1
                if absJ < minVal:
                    minVal = absJ
        if negCount % 2 == 1:
            return absSum - 2 * minVal
        else:
            return absSum