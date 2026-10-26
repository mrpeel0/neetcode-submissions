class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'u', 'o']
        l, r = 0, k
        maxvow = 0
        for x in s[l:r]:
            if x in vowels:
                maxvow +=1
        

        maxtemp = maxvow
        while r < len(s):
            if s[l] in vowels:
                maxtemp -= 1
            l +=1
                          
            if s[r] in vowels:
                maxtemp +=1
            r +=1 
            maxvow = max(maxtemp, maxvow)

        return maxvow 