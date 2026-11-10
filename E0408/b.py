# 输出整数列表最大的元素值，例如，整数列表[67, 4, 63, 43, 39, 7, 74, 62, 77, 55]最
# 大的元素值是77。（难度★✩✩✩✩） 
text = input("输入: ").strip("[]")
nums = [int(x.strip()) for x in text.split(",")]
new = sorted(nums,reverse = True)
print(new[0])