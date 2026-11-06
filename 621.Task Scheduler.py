class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        count=Counter(tasks)
        heap=[-x for x in count.values()]
        heapq.heapify(heap)
        q=deque()
        time=0
        while heap or q:
            time+=1
            if q and q[0][1]<=time:
                heapq.heappush(heap,q.popleft()[0])
            if heap:
                freq=heapq.heappop(heap)+1
                if freq<0:
                    q.append((freq,time+n+1))
        return time
        
