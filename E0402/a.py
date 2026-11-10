# 输出整数列表各元素的和。
# 测试： 
#  输入：[45, 80, 68, 70, 87, 73]，输出：423
text = input("输入: ").strip("[]")
new_text = text.split(",")
a = 0
for i in new_text:
    a += int(i)
print(a)