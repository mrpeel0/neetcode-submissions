class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sumlist = sum(nums)
        runsum = 0
        for x in range(len(nums)):
            if sumlist - nums[0] == 0:
                return x
            if runsum == sumlist - nums[x] - runsum:
                return x
            runsum += nums[x]
        return -1