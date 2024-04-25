# 给定两个数组 nums1 和 nums2 ，返回 它们的 交集。输出结果中的每个元素一定是 唯一 的。我们可以 不考虑输出结果的顺序 。

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 将两个列表转换为集合
        set1 = set(nums1)
        set2 = set(nums2)
        
        # 使用集合的交集操作来找出共有元素
        return list(set1 & set2)

# 示例使用
sol = Solution()
result = sol.intersection([1, 2, 2, 1], [2, 2])
print(result)  # 输出: [2]
