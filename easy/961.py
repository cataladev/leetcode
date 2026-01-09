class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(1,4):
            for j in range(len(nums) - i):
                if nums[j] == nums[j+i]:
                    return nums[j]