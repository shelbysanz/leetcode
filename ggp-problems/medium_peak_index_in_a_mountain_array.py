class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # approach: use binary search to find the peak
        l, r = 0, len(arr) - 1

        while l <= r:
            m = l + (r - l) // 2

            # check immediate neighbors of mid
            # case 1: both neighbors are smaller than mid => we found our peak
            if arr[m-1] < arr[m] and arr[m+1] < arr[m]:
                return m
            # case 2: left neighbor is smaller and right neighbor is larger, we are increasing, update left
            if arr[m-1] < arr[m] and arr[m+1] > arr[m]:
                l = m + 1
            # case 3: left neighbor is larger and right neighbor is smaller, we are decreasing, update right
            else:
                r = m

        # per leetcode, the arr is guaranteed to be a mountain, so we don't need to add anything here
