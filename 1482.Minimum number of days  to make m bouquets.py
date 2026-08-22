class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        low=min(bloomDay)
        high=max(bloomDay)
        ans=-1
        if len(bloomDay)<m*k:
            return -1
        def day(mid):
            bouquets=0
            flowers=0
            for bloom in bloomDay:
                if bloom<=mid:
                    flowers+=1
                    if flowers==k:
                        bouquets+=1
                        flowers=0
                else:
                    flowers=0
            return bouquets>=m
        while(low<=high):
            mid=(low+high)//2
            if day(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
