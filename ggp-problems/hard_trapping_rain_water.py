class Solution:
    def trap(self, height: List[int]) -> int:
        rain_count = 0
        n = len(height)

        def getBounds():
            bounds = [[0, 0] for _ in range(n)]
            l_max, r_max = 0, 0
            for i in range(n):
                l_max = max(l_max, height[i])
                bounds[i][0] = l_max
            for i in range(n - 1, -1, -1):
                r_max = max(r_max, height[i])
                bounds[i][1] = r_max
            return bounds

        bounds = getBounds()
        for i in range(1, n - 1):
            curr_height = height[i]
            l_bound, r_bound = bounds[i]
            bound = min(l_bound, r_bound)
            rain_count += max(0, bound - curr_height)
        return rain_count
