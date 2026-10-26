class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        maxlen = 1
        runlen = 1
        if not nums:
            return 0
        for x in range(1, len(nums)):
            if nums[x] - 1 == nums[x-1]:
                runlen += 1
                maxlen = max(maxlen, runlen)
            else:
                runlen = 1
        return maxlen