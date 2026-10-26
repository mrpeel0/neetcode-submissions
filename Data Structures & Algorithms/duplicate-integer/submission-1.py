class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        for x in nums:
            y = x
            numSame = 0
            for x in nums:
               

                if x == y:
                    numSame+=1
            if numSame > 1:
                return True

        
        return False