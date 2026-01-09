class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.help(nums[1:]), self.help(nums[:-1]))

    def help(self, nums):
        r1, r2 = 0,0
        for n in nums:
            new = max(n + r1, r2)
            r1 = r2
            r2 = new
        return r2
