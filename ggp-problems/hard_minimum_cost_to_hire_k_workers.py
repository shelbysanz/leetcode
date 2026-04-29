import heapq


class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        workers = []
        for q, w in zip(quality, wage):
            workers.append((w/q, q))

        workers.sort()
        heap = []
        quality_count, min_cost = 0, float('inf')
        for curr_ratio, curr_quality in workers:
            quality_count += curr_quality
            heapq.heappush(heap, -curr_quality)  # using negative to make max heap

            while len(heap) > k:
                quality_count += heapq.heappop(heap)

            if len(heap) == k:
                min_cost = min(min_cost, curr_ratio * quality_count)

        return min_cost
