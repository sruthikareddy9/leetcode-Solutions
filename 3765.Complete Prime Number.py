class Solution:
    def completePrime(self, num: int) -> bool:
        def is_prime(n):
            if n<2:
                return False
            for i in range(2,int(n**0.5)+1):
                if n%i==0:
                    return False
            return True
        s=str(num)
            #check prefix
        for i in range(1,len(s)+1):
            if not is_prime(int(s[:i])):
                return False
            #check suffix
        for i in range(1,len(s)):
            if not is_prime(int(s[i:])):
                return False
        return True
        
