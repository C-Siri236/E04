#  假设整数列表中至少有两个不同的值，输出该列表中第二大的元素值。例如，整
# 数列表[10, 5, 20, 30, 6]中第二大的元素值是20。
text = input("输入: ").strip("[]")
nums = [int(x.strip()) for x in text.split(",")]
new = sorted(nums,reverse = True)
print(new[1])