# 回文列表。如果一个列表从左往右读和从右往左读是一样的，就称这个列表为回文
# 列表。编写程序，判断给定的列表是否是回文列表。例如，[“One”, “Test”, “ – ”, “Test”, 
# “One”]是回文列表，[“Tim”, “Tom”, “Mike”, “Max”]不是回文列表
import ast

a = ast.literal_eval(input("输入列表: "))

if a[::-1] == a:
    print(f"{a}是回文列表")
else:
    print(f"{a}不是回文列表")