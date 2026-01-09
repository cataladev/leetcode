class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        for row in grid:
            first = len(row)
            for i, value in enumerate(row):
                if value < 0:
                    first = i
                    break
            count += len(row) - first
        return count