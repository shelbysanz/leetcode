class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            array_count = 1
            curr_sum = 0
            for i in nums:
                curr_sum += i
                if curr_sum > largest:
                    array_count += 1
                    curr_sum = i
            return array_count <= k

        l, r = max(nums), sum(nums)
        min_sum = r
        while l <= r:
            m = l + (r - l) // 2
            if canSplit(m):
                min_sum = m
                r = m - 1
            else:
                l = m + 1
        return min_sum
