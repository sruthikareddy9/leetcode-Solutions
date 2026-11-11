class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        heap=[(-v,k)for k,v in count.items()]
        heapq.heapify(heap)
        res=[]
        prev=None
        while heap:
            f, ch = heapq.heappop(heap)
            res.append(ch)
            if prev:
                heapq.heappush(heap, prev)
            f += 1
            prev = (f, ch) if f < 0 else None

        return "".join(res) if len(res) == len(s) else ""
        
