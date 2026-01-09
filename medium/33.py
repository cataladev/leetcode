class Solution:
    def bSearch(self, nums, target, start, end):
        while start <= end:
            middle = (start + end) // 2
            if nums[middle] == target:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
        return -1
    def pivot(self, nums):
        start = 0
        end = len(nums) - 1
        while start < end:
            middle = (start + end) // 2
            if nums[middle] > nums[end]:
                start = middle + 1
            else:
                end = middle
        return start
    def search(self, nums: List[int], target: int) -> int:
        piv = self.pivot(nums)
        if target == nums[piv]:
            return piv
        elif nums[0] <= target <= nums[piv - 1 if piv > 0 else 0]:
            return self.bSearch(nums, target, start = 0, end = piv - 1)
        else:
            return self.bSearch(nums, target, start = piv, end =len(nums)- 1)