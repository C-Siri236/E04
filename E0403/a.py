# 将整数列表的元素按照升序排列后输出。（难度★★✩✩✩） 
# 测试： 
#  输入：[49, 56, 44, 0]，输出：[0, 44, 49, 56] 
#  输入：[15]，输出：[15] 
text = input("输入: ").strip("[]")
new_text = text.split(", ")
new_text.sort()
print(f"[{", ".join(new_text)}]")