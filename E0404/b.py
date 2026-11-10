# 列表逆序。输入一个列表，将其元素逆序排列后输出。例如，输入[1, 2, 3, 4]，输出 
# [4, 3, 2, 1]。（ 难 度 ★★✩✩✩） 
import ast

list1 = ast.literal_eval(input("输入列表: "))

my_list = sorted(list1, reverse=True)
print(my_list)