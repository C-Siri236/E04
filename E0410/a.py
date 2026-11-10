# 输入正整数n，输出n阶杨辉三角
def f(n):
    if n == 1:
        return [1]
    pre = f(n - 1)
    cur = [1]
    for i in range(len(pre) - 1):
        cur.append(pre[i] + pre[i+1])
    cur.append(1)
    return cur

n = int(input("输入正整数: "))
for i in range(1, n + 1):
    row = f(i)
    print(" ".join(map(str,row)))



