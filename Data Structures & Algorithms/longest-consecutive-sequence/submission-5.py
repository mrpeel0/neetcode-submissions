class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        print(nums)
        length = 1
        x = 1
        list1 = [1]
        if nums == []:
            return 0
        while x < len(nums):
            if nums[x-1] + 1 == nums[x]:
                length +=1
                if x == len(nums)-1:
                    list1.append(length)
            else:
                list1.append(length)
                length = 1
            x+=1
        return max(list1)
