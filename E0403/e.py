
#  给定一个列表的列表，将其按照子列表元素之和排序。
# 例如，[[45, 16, 81, 87] , [22, 38], [67, 78], [48, 63, 29]]
# 排序后得到[[22, 38], [48, 63, 29] , [67, 78], [45, 16, 81, 87]]
import ast

text = input("输入: ")
my_list = ast.literal_eval(text)

my_list.sort(key=sum)

print(my_list)

