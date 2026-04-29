import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickselect(l, r):
            while True:
                if r == l:
                    return nums[l]

                pivot = nums[random.randint(l, r)]

                l_tmp, r_tmp = l, r
                while l_tmp <= r_tmp:
                    while nums[l_tmp] < pivot:
                        l_tmp += 1
                    while nums[r_tmp] > pivot:
                        r_tmp -= 1

                    if l_tmp <= r_tmp:
                        nums[l_tmp], nums[r_tmp] = nums[r_tmp], nums[l_tmp]
                        l_tmp += 1
                        r_tmp -= 1

                if k >= l_tmp:
                    l = l_tmp
                elif k <= r_tmp:
                    r = r_tmp
                else:
                    return nums[k]

        return quickselect(0, len(nums) - 1)
