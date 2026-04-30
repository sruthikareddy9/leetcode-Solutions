class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res=[]
        def helper(start,curr_sum,path):
            if curr_sum==target:
                res.append(path[:])
                return
            if curr_sum>target:
                return
            for i in range(start,len(candidates)):
                if i>start and candidates[i]==candidates[i-1]:
                    continue
                path.append(candidates[i])
                helper(i+1,curr_sum+candidates[i],path)
                path.pop()
        helper(0,0,[])
        return res
