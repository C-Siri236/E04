# 求两个列表a、b的共同元素。要求输出结果时，元素出现的顺序与其在列表a中
# 的顺序相同。
import ast

a = ast.literal_eval(input("输入列表: "))
b = ast.literal_eval(input("输入列表: "))

result = []
for x in a:

    if x in b and x not in result:
        result.append(x)

print(result)  