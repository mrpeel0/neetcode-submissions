class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        listoutput = []
        zeroindexes = []
        bigval = 1
        x = 0;
        while x < len(nums):
            if nums[x] == 0:
                zeroindexes.append(x)
                
            else: 
                bigval *= nums[x]
            x +=1 
        x = 0
        while x < len(nums):
            if len(zeroindexes) >1:
                for n in nums:
                    listoutput.append(0)
                return listoutput
            elif x in zeroindexes:
                listoutput.append(bigval)
            elif len(zeroindexes) > 0:
                listoutput.append(0)
            else:
                listoutput.append(int(bigval/nums[x]))
            x +=1
        return listoutput
            