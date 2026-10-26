class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            num1 = nums[i]
            y = i + 1
            while y < len(nums):
                num2 = num1 + nums[y]
                if num2 == target:
                    return [i, y]
                y +=1
            i += 1