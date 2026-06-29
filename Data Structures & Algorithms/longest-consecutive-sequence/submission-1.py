class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlen = 0
        for num in numset:
            if num - 1 not in numset:
                curr = num
                chain = 1 
                while curr + 1 in numset:
                    curr += 1
                    chain += 1 
                maxlen = max(maxlen, chain)
        return maxlen
