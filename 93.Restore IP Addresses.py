class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res=[]
        def backtrack(index,path):
            if len(path)==4:
                if index==len(s):
                    res.append(".".join(path))
                return res
            for i in range(1,4):
                if index+1>len(s):
                    break
                part=s[index:index+i]
                if len(part)>1 and part[0]=='0':
                    continue
                if int(part)<=255:
                    backtrack(index+i,path+[part])
        backtrack(0,[])
        return res
        
