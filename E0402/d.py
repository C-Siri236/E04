#  将整数列表的第1个元素加上第2个元素，然后减去第3个元素，再加上第4个
# 元素，…，依次类推，求计算结果。
# 例如：对应列表[10, 20, 30, 40, 50, 60]的计算公
# 式是10+20-30+40-50+60，计算结果是50。（ 难 度 ★✩✩✩✩） 
text = input("输入: ").strip("[]")
new_text = text.split(",")
a = 0
for i in new_text:
    a += 1
total = int(new_text[0])
for j in range(1,int(a)):
    if j % 2 == 0:
        total -= int(new_text[j])
    else:
        total += int(new_text[j])
print(total)