# 将整数列表中的偶数放在奇数之前，放置整数时无需保持原有顺序
text = input("输入: ").strip("[]")
nums = [int(x.strip()) for x in text.split(",")]
a = []
b = []
for i in nums:
    if i % 2 == 0:
        a.append(i)
    else:
        b.append(i)
print(a + b)
