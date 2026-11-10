
import ast

list1 = ast.literal_eval(input("输入列表: "))


target = int(input("输入要删除的值: "))


while target in list1:
    list1.remove(target)

print(list1)