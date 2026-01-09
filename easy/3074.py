class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total = sum(apple)
        i = 0
        while i < len(capacity):
            if total > 0:
                total -= capacity[i]
            else:
                return i
            i += 1
        return i