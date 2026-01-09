class Solution:
    def numOfWays(self, n: int) -> int:
        twos = 6
        threes = 6

        MOD = 1e9 + 7

        for _ in range(1,n):
            new_twos = twos * 3 + threes * 2
            new_threes = twos * 2 + threes * 2

            twos = new_twos % MOD
            threes = new_threes % MOD

        return int((twos + threes) % MOD)