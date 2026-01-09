class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for x in nums:
            count = 0
            dsum = 0
            i = 1
            while i * i <= x:
                if x % i == 0:
                    j = x // i
                    count += 1
                    dsum += i
                    if i != j:
                        count += 1
                        dsum += j
                    if count > 4:
                        break
                i += 1
            if count == 4:
                total += dsum
        return total
