
from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        countAB = defaultdict(int)
        
        # 计算 nums1 和 nums2 所有元素对的和及其出现次数
        for a in nums1:
            for b in nums2:
                sumAB = a + b
                countAB[sumAB] += 1
        
        result = 0
        
        # 计算 nums3 和 nums4 所有元素对的和，查看是否有和为负的数已经在哈希表中
        for c in nums3:
            for d in nums4:
                sumCD = c + d
                result += countAB[-sumCD]
        
        return result

# 示例使用
sol = Solution()
result = sol.fourSumCount([1,2],[-2,-1],[-1,2],[0,2])
print(result)  # 应该输出 2
