#  删除重复。输入一个列表，将其中重复出现的元素删除后输出。
# 例如，输入[1, 1, 2, 3, 4, 1, 2, 3]输出[1, 2, 3, 4]，
# 输入[7, 5, 3, 5, 1]输出[7, 5, 3, 1]，输入[1, 1, 1, 1]输出[1]。
# （难度★★✩✩✩）
import ast

lst = ast.literal_eval(input("输入列表: "))
result = []


for item in lst:
    if item not in result:
        result.append(item)

print(result)