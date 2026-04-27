class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
        res=[]
        for i in range(len(nums)):
            curr=nums[i]
            remain=nums[:i]+nums[i+1:]
            for p in self.permute(remain):
                res.append([curr]+p)
        return res
