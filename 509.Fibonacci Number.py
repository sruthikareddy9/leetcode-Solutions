class Solution:
    def fib(self,n):
        memo={}
        def helper(n):
            if n in memo:
                return memo[n]
            if n<=1:
                return n
            memo[n]=helper(n-1)+helper(n-2)
            return memo[n]
        return helper(n)
        
