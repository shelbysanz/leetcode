from collections import deque


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # base case
        if not fruits:
            return 0

        # variable that holds max fruits possible, variable that holds the how many so far, current count of same type consecutive
        max_fruits, curr_count, curr_consecutive = 0, 0, [fruits[0], 0]
        # type array, the current valid two types of fruits
        fruit_types = deque([None, fruits[0]])

        for i in fruits:
            if i not in fruit_types:
                fruit_types.popleft()
                fruit_types.append(i)
                curr_count = curr_consecutive[1]

            # the most recent seen should be latest in the fruit_type list, keeping track of fruit group
            if fruit_types[-1] != i:
                fruit_types.popleft()
                fruit_types.append(i)

            curr_count += 1

            # keep track of max fruits in basket possible
            max_fruits = max(max_fruits, curr_count)

            # if not consecutive restart consecutive count
            if curr_consecutive[0] == i:
                curr_consecutive[1] += 1
            else:
                curr_consecutive = [i, 1]

        return max_fruits
