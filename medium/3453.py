class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        low, high, tot = float('inf'), float('-inf'), 0

        for x, y, l in squares:
            tot += l*l
            low = min(low, y)
            high = max(high, y + l)
        
        target = tot / 2.0

        for i in range(60):
            mid = (low+high) / 2.0

            curr_area = 0
            for _, y, l in squares:
                curr_y = max(0, min(l, mid-y))
                curr_area += l*curr_y
            
            if curr_area < target:
                low = mid
            else:
                high = mid
        return mid