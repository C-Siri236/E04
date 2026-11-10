#  整数列表中包含正数和负数，将该整数列表的元素按照绝对值降序排列后输出。
# 例如，[37, 4, -27, 22, -79]排序后得到[-79, 37, -27, 22, 4]。（ 难 度 ★★✩✩✩） 

text = input("输入: ").strip("[]")
nums = [int(x) for x in text.split(",")] 

result = sorted(nums, key=abs, reverse=True)

print(result)
