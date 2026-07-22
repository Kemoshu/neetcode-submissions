class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        lst = []
        sort_lst = []
        nums.sort()
        for i in range(len(nums[:-2])):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[left] + nums[i] + nums[right] == 0:
                    hld = [nums[left], nums[i], nums[right]]
                    hld.sort()
                    if hld not in sort_lst:
                        sort_lst.append(hld)
                        lst.append([nums[left], nums[i], nums[right]])
                    left += 1
                    right -= 1
                if nums[left] + nums[i] + nums[right] < 0:
                    left += 1    
                elif nums[left] + nums[i] + nums[right] > 0:
                    right -= 1
        return lst