class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)):
            y= x+1
            while y < len(nums):
                if nums[x] + nums[y] == target:
                    return [x, y]
                y +=1
