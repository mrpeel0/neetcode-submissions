class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for x in s:
            if t.find(x) != -1:
                t = t[:t.find(x)] + t[t.find(x)+1:]
                continue
            else:
                return False
        return True