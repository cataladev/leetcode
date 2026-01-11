class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        ans = 0

        for top in range(n):
            good = [1] * m   # good[c] means column c is all 1s from top..bot
            for bot in range(top, n):
                # update good for this new bottom row
                for c in range(m):
                    good[c] &= (matrix[bot][c] == '1')

                # longest consecutive 1s in good
                best_width = 0
                cur = 0
                for c in range(m):
                    if good[c]:
                        cur += 1
                        if cur > best_width:
                            best_width = cur
                    else:
                        cur = 0

                height = bot - top + 1
                ans = max(ans, height * best_width)

        return ans