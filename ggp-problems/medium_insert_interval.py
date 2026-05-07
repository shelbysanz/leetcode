class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        output = []
        i, n = 0, len(intervals)

        new_start, new_end = newInterval

        # left
        while i < n and intervals[i][1] < new_start:
            output.append(intervals[i])
            i += 1

        # merge
        while i < n and intervals[i][0] <= new_end:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1

        output.append([new_start, new_end])

        # right
        while i < n:
            output.append(intervals[i])
            i += 1

        return output
