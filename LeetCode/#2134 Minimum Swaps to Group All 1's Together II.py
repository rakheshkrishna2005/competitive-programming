class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total_ones = sum(nums)
        
        if total_ones == 0 or total_ones == len(nums):
            return 0
        
        doubled_nums = nums + nums
        window_ones = sum(doubled_nums[:total_ones])
        max_ones = window_ones
        
        for i in range(total_ones, len(doubled_nums)):
            window_ones += doubled_nums[i] - doubled_nums[i - total_ones]
            max_ones = max(max_ones, window_ones)
        
        return total_ones - max_ones
