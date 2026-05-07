class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        found = -1
        # find first
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] >= target:
                if nums[m] == target:
                    found = m
                r = m - 1
            else:
                l = m + 1
        first = found

        l, r = 0, len(nums) - 1
        found = -1
        # find last
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] <= target:
                if nums[m] == target:
                    found = m
                l = m + 1
            else:
                r = m - 1
        last = found

        return [first, last]
