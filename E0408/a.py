# 输出整数列表最小元素值所在的位置。如果最小值不止一个，输出最小的位置。（难
# 度★✩✩✩✩） 
# 测试： 
#  输入：[5, 11, 8, 5, 13, 38]，输出：0 
#  输入：[5, 3, 4, 2, 6, 7, 8, 9, 1, 10]，输出：8 
text = input("输入: ").strip("[]")
nums = [int(x.strip()) for x in text.split(",")]
new = sorted(nums)
n = len(nums)
min = new[0]
for i in range(n):
    if nums[i] == min:
        print(i)
        break