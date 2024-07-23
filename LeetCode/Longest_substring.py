
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        listString: list  = list(s)
        indexArray: list = [None]*1000
        sub: list[str] = []
        res = 0
        for item in listString:
            if indexArray[ord(item)] != None:
                if res < len(sub):
                    res = len(sub)
                sub = []
                indexArray= [None]*1000
            indexArray[ord(item)] = 1
            sub.append(item)
        if res < len(sub):
            res = len(sub)
        return res
        
sol: Solution = Solution()
res : int = sol.lengthOfLongestSubstring(s="dvdf")
print(res)