# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。

# 注意：答案中不可以包含重复的三元组。

# 哈希法
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        seen = set()
        
        for i in range(len(nums)):
            if nums[i] in seen:
                continue
            seen.add(nums[i])
            target = -nums[i]
            num_dict = {}
            for j in range(i + 1, len(nums)):
                if nums[j] in num_dict:
                    triple = [nums[i], nums[j], -nums[i] - nums[j]]
                    triple.sort()
                    result.append(triple)
                num_dict[target - nums[j]] = j
                
        return result

# 双指针法
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # 跳过重复的数字
            l, r = i + 1, n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1  # 跳过重复的数字
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1  # 跳过重复的数字
                    l += 1
                    r -= 1
        
        return result
