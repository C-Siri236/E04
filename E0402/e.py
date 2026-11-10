#  求整数列表中所有的元素对，这些元素对的和能被指定的整数整除。
# 例如，[1, 2, 3, 4, 5, 6]中能被5整除的元素对有：(1,4), (2,3),(4,6)。（难度★★✩✩✩） 
text = input("输入: ").strip("[]")
n = int(input("指定的整数: "))
new_text = text.split(",")
result = []
a = len(new_text)
for j in range(int(a)):
    b = int(new_text[j])
    for r in range(j + 1, int(a)):
        if (b + int(new_text[r]))% n == 0:
            result.append(f"({int(new_text[j])},{int(new_text[r])})")
print(", ".join(result))
        

