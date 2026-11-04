class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        heap=[]
        for i in range(len(matrix)):
            heapq.heappush(heap,(matrix[i][0],i,0))
        for _ in range(k):
            val,row,col=heapq.heappop(heap)
            if col+1<len(matrix):
                heapq.heappush(heap,(matrix[row][col+1],row,col+1))
        return val
        
