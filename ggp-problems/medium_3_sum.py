class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        triplets = []

        # implement logic
        nums.sort()
        for idx in range(0, n - 2):
            # if current value is same as previous value, need to skip the iteration
            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue

            left, right = idx + 1, n - 1
            while left < right:
                curr_sum = nums[idx] + nums[left] + nums[right]

                if curr_sum == 0:
                    triplets.append([nums[idx], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    # make sure duplicates are skipped
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                    continue

                # if curr sum > 0, move right pointer (should decrease val)
                if curr_sum > 0:
                    right -= 1
                # else move left pointer (should increase val)
                else:
                    left += 1

        return triplets
