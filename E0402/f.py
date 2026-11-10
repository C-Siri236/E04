#  假设列表由整数和字符串组成。求列表中整数元素和可以转换为整数的字符串元
# 素之和。例如，列表是[10, 20, 'a', '30', 'bcd']时输出60。（难度★★✩✩✩）
text = input("输入: ").strip("[]")
new_text = text.split(",")
total = 0
for i in new_text:
    clean_i = i.strip().strip("'\"")
    try:
        num = int(clean_i)
        total += num
    except ValueError:
        pass
print(total)
