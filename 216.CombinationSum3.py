class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        res=[]
        def helper(start,curr_sum,path):
            if len(path)==k and curr_sum==n:
                res.append(path[:])
                return
            if curr_sum>n or len(path)>k:
                return
            for i in range(start,len(nums)):
                path.append(nums[i])
                helper(i+1,curr_sum+nums[i],path)
                path.pop()
        helper(0,0,[])
        return res
        
