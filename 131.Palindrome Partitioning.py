class Solution:
    def partition(self, s: str):
        res = []
        def isPalindrome(sub):
            l, r = 0, len(sub)-1
            while l < r:
                if sub[l] != sub[r]:
                    return False
                l += 1
                r -= 1
            return True
        def backtrack(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if isPalindrome(sub):
                    path.append(sub)
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return res
