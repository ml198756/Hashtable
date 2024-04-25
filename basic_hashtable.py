# 哈希表通过字典来实现
count = {}  # 初始为空字典

for num in [1, 2, 2, 3]:
    if num in count:
        count[num] += 1
    else:
        count[num] = 1


# 比如你要计数多个项的出现次数，如果使用普通的字典，你需要写出如下代码：
count = {}
data = [1, 2, 2, 3, 3, 3]
for item in data:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

# 使用 defaultdict(int)，你可以简化为：
count = defaultdict(int)
data = [1, 2, 2, 3, 3, 3]
for item in data:
    count[item] += 1
