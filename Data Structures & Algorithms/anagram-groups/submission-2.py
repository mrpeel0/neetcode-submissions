class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortdict = {}
        for word in strs:
            s = "".join(sorted(word))
            if s in sortdict:
                sortdict[s].append(word)
            else:
                sortdict[s] = [word]
        
        return list(sortdict.values())