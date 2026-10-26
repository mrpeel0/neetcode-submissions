class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currsum = 0
        prevsum = {0 : 1}
        total = 0

        for num in nums:
            currsum += num
            diff = currsum - k

            total += prevsum.get(diff, 0)

            prevsum[currsum] = prevsum.get(currsum, 0) + 1

        return total