class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        len1 = 0
        for l in range(l, len(s2)):
            temp = list(s1)
            len1 = 0
            while l < len(s2) and s2[l] in temp:

                temp.remove(s2[l])

                l+=1
                len1 +=1
                if len1 == len(s1):
                    return True
        return False