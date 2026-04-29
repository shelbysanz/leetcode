class Solution:
    def trap(self, height: List[int]) -> int:
        rain_count = 0
        n = len(height)
        for i in range(1, n - 1):
            curr_height = height[i]
            l, r = i - 1, i + 1
            l_bound, r_bound = height[l], height[r]
            while l >= 0:
                l_bnd = height[l]
                if l_bnd > l_bound:
                    l_bound = l_bnd
                l -= 1
            while r < n:
                r_bnd = height[r]
                if r_bnd > r_bound:
                    r_bound = r_bnd
                r += 1
            bound = min(l_bound, r_bound)
            rain_count += max(0, bound - curr_height)
        return rain_count
