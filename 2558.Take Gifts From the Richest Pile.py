class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        maxHeap=[-x for x in gifts]
        heapq.heapify(maxHeap)
        for i in range(k):
            largest=-heapq.heappop(maxHeap)
            remaining=math.isqrt(largest)
            heapq.heappush(maxHeap,-remaining)
        return -sum(maxHeap)
