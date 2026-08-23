class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        ans=-1
        while(low<=high):
            mid=(low+high)//2
            total=sum((num+mid-1)// mid for num in nums)
            if total<=threshold:
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans
