class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for x in count:
            if count[x] == 1:
                return s.index(x)
        return -1