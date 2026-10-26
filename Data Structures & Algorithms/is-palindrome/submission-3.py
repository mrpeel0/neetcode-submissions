class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        newstring=[]
        for char in s:
            if char.isalnum():
                newstring.append(char.lower())
        print(newstring)
        half = len(newstring)//2
        otherside = newstring[::-1]
        if newstring[:half] == otherside[:half]:
            return True
        else:
            return False