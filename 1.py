# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 哈希表用于存储数组元素和它们的索引
        num_dict = {}
        
        # 遍历数组中的每个元素
        for i, num in enumerate(nums):
            # 计算差值
            complement = target - num
            # 如果差值在哈希表中存在，那么我们找到了两个数
            if complement in num_dict:
                return [num_dict[complement], i]
            # 如果不存在，将当前元素及其索引添加到哈希表中
            num_dict[num] = i
        
        # 如果遍历完成没有找到结果，按题目描述这种情况不会发生
        return []

# 示例使用
sol = Solution()
print(sol.twoSum([2, 7, 11, 15], 9))  # 输出: [0, 1]
