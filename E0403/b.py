# 对整数列表进行排序，要求偶数位置的元素升序排列，奇数位置的元素降序排列。
# 例如，[37, 4, 27, 22, 79]排序后得到[27, 22, 37, 4, 79]。（ 难 度 ★★✩✩✩） 
text = input("输入: ").strip("[]")
new_text = [int(x) for x in text.split(",")] 

a = new_text[::2]
ou = sorted(a)
n = len(a)
b = new_text[1::2]
ji = sorted(b, reverse=True)
result = []
for i in range(n):
    result.append(ou[i]) 
    if i < len(ji): 
        result.append(ji[i])
print(result)
print(new_text)    