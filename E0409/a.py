# 给定一个整数列表a和一个参考整数值r，输出列表b，要求在列表b中，列表a
# 中小于r的元素在r左边，大于等于r的元素在r右边， 不要求列表b中的元素保
# 持它们在列表a中的顺序。
import ast

a = ast.literal_eval(input("给定一个整数列表: "))
r = int(input("参考整数值: "))
min_ = []
max_ = []
for i in a:
    if i < r:
        min_.append(i)
    else:
        max_.append(i)
n = len(min_)
result = min_ + max_
result.insert(n, r)
print(result)

