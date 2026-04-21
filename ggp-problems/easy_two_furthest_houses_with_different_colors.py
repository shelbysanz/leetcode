class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        max_len = float('-inf')
        color = colors[-1]
        for i in range(len(colors) - 1):
            if colors[i] != color:
                max_len = max(max_len, abs(len(colors) - 1 - i))
        color = colors[0]
        for i in range(len(colors) - 1, 0, -1):
            if colors[i] != color:
                max_len = max(max_len, abs(0 - i))
        return max_len
