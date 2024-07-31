class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i

        for i in range(len(nums)):
            x = target - nums[i]
            if x in d and i != d[x]:
                return [i, d[x]]
