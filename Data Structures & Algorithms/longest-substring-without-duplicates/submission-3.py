class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        maxlen = 1
        for x in range(l, r):
            while r < len(s):
                while s[r] in s[l:r]:
                    l += 1
                r +=1
                    
                if len(s[l:r]) > maxlen:
                    maxlen = len(s[l:r])
        if s:       
            return maxlen
        return 0