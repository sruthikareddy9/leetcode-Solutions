class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        def helper(start,curr_sum,path):
            if curr_sum==target:
                res.append(path[:])
                return
            if curr_sum>target:
                return
            for i in range(start,len(candidates)):
                path.append(candidates[i])
                helper(i,curr_sum+candidates[i],path)
                path.pop()
        helper(0,0,[])
        return res
