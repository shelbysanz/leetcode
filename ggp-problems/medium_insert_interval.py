class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        l, r = 0, len(intervals)
        while l < r:
            m = l + (r - l) // 2
            if intervals[m][1] < newInterval[0]:
                l = m + 1
            else:
                r = m
        start = l
        output = intervals[:start]

        i = start
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        output.append(newInterval)
        output.extend(intervals[i:])

        return output
