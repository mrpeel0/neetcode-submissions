class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        s = 0
        e = len(numbers) -1
        while e != s:
            if numbers[s] + numbers[e] > target:
                e -=1

            elif numbers[s] + numbers[e] < target:
                s +=1

            else:
                outputlist = [s+1, e+1]
                return outputlist