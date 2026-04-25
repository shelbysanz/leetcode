class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [float('-inf')] * len(nums)
        for i in range(n):
            if i == 0:
                dp[i] = nums[i]
                continue
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        return max(dp)
