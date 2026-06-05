class Solution:
    def isValid(self,s):
     prev=None
     while s and s!=prev:
        prev=s
        s=s.replace("()","").replace("{}","").replace("[]","")
     return s==""
