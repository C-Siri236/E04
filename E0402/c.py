# 输出整数列表中偶数位置的元素之和。
# 例如，整数列表[10, 5, 21, 30, 6]偶数位置
# 的元素之和是37。（难度★✩✩✩✩）
text = input("输入: ").strip("[]")
new_text = text.split(",")
a = 0
for i in new_text:
    a += 1
total = 0
for i in range(int(a)):
    if i % 2 == 0:
        total += int(new_text[i])
print(total)


