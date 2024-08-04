class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        subarray_sum = []

        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sum.append(current_sum)
        
        subarray_sum.sort()

        result = 0
        for i in range(left - 1, right):
            result = (result + subarray_sum[i]) % MOD

        return result
