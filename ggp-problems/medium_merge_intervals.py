class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        def isOverlapping(prev, curr):
            # [start, end]
            return curr[0] <= prev[1]

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]
        # process in order, for each check if it overlaps with the last end time
        for i in range(1, len(intervals)):
            curr = intervals[i]
            prev = output[-1]
            if isOverlapping(prev, curr):  # if overlapping, merge, update previous
                # merge
                output[-1][0] = min(curr[0], prev[0])
                output[-1][1] = max(curr[1], prev[1])
            else:
                output.append(curr)

        return output
