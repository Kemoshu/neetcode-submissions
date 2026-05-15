class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dct = {}
        for i in set(nums):
            dct[i] = nums.count(i)
        lst = sorted(dct, key=lambda x: dct[x], reverse=True)
        ans = lst[:k]
        return ans