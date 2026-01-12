class Solution:
    def knightDialer(self, n: int) -> int:
        MOD = 10**9 + 7
        current_count = [1] * 10
        for _ in range(n - 1):
            next_count = [0] * 10
            next_count[0] = current_count[4] + current_count[6]
            next_count[1] = current_count[6] + current_count[8]
            next_count[2] = current_count[7] + current_count[9]
            next_count[3] = current_count[4] + current_count[8]
            next_count[4] = current_count[0] + current_count[3] + current_count[9]
            # next_count[5] remains 0
            next_count[6] = current_count[0] + current_count[1] + current_count[7]
            next_count[7] = current_count[2] + current_count[6]
            next_count[8] = current_count[1] + current_count[3]
            next_count[9] = current_count[2] + current_count[4]
            current_count = next_count
        return sum(current_count) % MOD