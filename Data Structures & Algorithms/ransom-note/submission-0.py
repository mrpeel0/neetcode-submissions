class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = list(ransomNote)
        for x in magazine:
            if x in ransomNote:
                ransomNote.remove(x)
            if not ransomNote:
                return True
        return False