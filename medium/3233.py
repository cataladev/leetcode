class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        # if number is special it satisfys n == p**2 p is prime

        def is_prime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for i in range(2, int(sqrt(num)) + 2):
                if num % i == 0:
                    return False
            return True
        
        count = 0
        start = int(sqrt(l))
        end = int (sqrt(r))
        for n in range(start, end + 1):
            if n ** 2 >= l and n ** 2 <= r:
                if is_prime(n):
                    count += 1
        return r - l + 1 - count