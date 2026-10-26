class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countedlist = Counter(nums)
        outputlist = []
        list1 = sorted(countedlist.items(), key = lambda pair: pair[1], reverse = True)[:k]
        for x in list1:
            outputlist.append(x[0])

        return outputlist