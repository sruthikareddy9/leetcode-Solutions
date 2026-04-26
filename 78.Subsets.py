# leetcode-Solutions
My Leetcode problem solutions in python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def bt(start,path):
            res.append(path[:])
            for i in range(start,len(nums)):
                path.append(nums[i])
                bt(i+1,path)
                path.pop()
        bt(0,[])
        return res
