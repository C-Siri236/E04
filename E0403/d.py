#  给定一个字符串列表，将其按照字符串中包含的元音字母个数排序。
# 例如，[“hello“, “world“, “banana“, “at“]排序后得到[“at“, “world“, “hello“, “banana“]。（ 难 度 ★★✩✩
text = input("输入: ").strip("[]")
new_text = [x.strip().strip("“") for x in text.split(",")]
letter = "a", "e", "i", "o", "u"
n = len(new_text)
d = {}
for i in range(n):
    a = 0
    for j in new_text[i]:
        if j in letter:
            a += 1
    d[new_text[i]] = a
sorted_items = sorted(d.items(), key=lambda x: x[1])
result = [item[0] for item in sorted_items]
print(result)

    