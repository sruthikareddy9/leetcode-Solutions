class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(curr,open,close):
            if len(curr)==2*n:
                res.append(curr)
                return
            if open<n:
                helper(curr+"(",open+1,close)
            if close<open:
                helper(curr+")",open,close+1)
        helper("",0,0)
        return res
