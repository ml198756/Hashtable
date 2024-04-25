# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # 如果长度不同，直接返回False
        if len(s) != len(t):
            return False
        
        # 使用字典来记录每个字符的出现次数
        count = {}
        
        # 统计字符串 s 中每个字符的出现次数
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        # 遍历字符串 t，减少计数
        for char in t:
            if char in count:
                count[char] -= 1
                # 如果某字符计数为负，则说明 t 中该字符比 s 中多，直接返回 False
                if count[char] < 0:
                    return False
            else:
                # 如果 t 中出现 s 中没有的字符，也返回 False
                return False
        
        # 如果所有字符的计数都归零，则返回 True
        return all(x == 0 for x in count.values())

# 示例使用
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  # 输出: True
print(sol.isAnagram("rat", "car"))  # 输出: False
