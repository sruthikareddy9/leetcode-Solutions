class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        def bt(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                else:
                    path.append(nums[i])
                    bt(i+1,path)
                    path.pop()
        bt(0,[])
        return res
        
