# 四数之和

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()  # 首先排序
        results = []
        n = len(nums)

        # 遍历数组，固定第一个和第二个数
        for i in range(n):
            # 跳过重复的元素
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n):
                # 跳过重复的元素
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # 使用双指针寻找后两个数
                l, r = j + 1, n - 1
                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total < target:
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        results.append([nums[i], nums[j], nums[l], nums[r]])
                        # 跳过重复的元素
                        while l < r and nums[l] == nums[l + 1]:
                            l += 1
                        while l < r and nums[r] == nums[r - 1]:
                            r -= 1
                        l += 1
                        r -= 1

        return results
