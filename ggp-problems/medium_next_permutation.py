class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # assumption: leetcode constraints guarantee atleast one element

        n = len(nums)

        # find pivot
        pivot = None
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # if no pivot, reverse the array
        if pivot is None:
            nums.reverse()
            return

        # otherwise, get next order number
        for i in range(n - 1, pivot, -1):
            if nums[i] > nums[pivot]:
                # swap
                nums[pivot], nums[i] = nums[i], nums[pivot]
                break

        # for container reverse the sorted array
        left, right = pivot + 1, n - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
