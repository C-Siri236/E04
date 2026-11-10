# 输出列表开头元素和结尾元素构成的子列表。
# 测试： 
#  输入：[53, 59, 77, 68, 74, 9, 10]，输出：[53, 10] 
#  输入：[71]，输出：[71]
text = input("输入: ").strip("[]")
my_list = text.split(",")
if len(my_list) == 1:
    print(f"[{my_list[0].strip()}]")
else:
    print(f"[{my_list[0].strip()},{my_list[-1].strip()}]")
    print(my_list)