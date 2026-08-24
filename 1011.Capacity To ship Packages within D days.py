class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low=max(weights)
        high=sum(weights)
        while low<=high:
            mid=(low+high)//2
            current_weight=0
            noofdays=1
            for weight in weights:
                if current_weight+weight>mid:
                    noofdays+=1
                    current_weight=0
                current_weight+=weight
            if noofdays<=days:
                high=mid-1
            else:
                low=mid+1
        return low
