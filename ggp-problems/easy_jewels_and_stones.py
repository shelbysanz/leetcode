class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # the jewels can be added to a set for constant look up afterwards
        jewel_bag = set(jewels)

        jewel_count = 0
        for i in stones:
            if i in jewel_bag:
                jewel_count += 1

        return jewel_count
