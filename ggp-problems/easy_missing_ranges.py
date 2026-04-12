class Solution:
    def findMissingRanges(
        self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        pointer = lower
        intervals = []
        for i in nums:
            if pointer < i:
                ending = min(i - 1, upper)
                intervals.append([pointer, ending])
            pointer = i + 1
        if pointer <= upper:
            intervals.append([pointer, upper])
        return intervals
