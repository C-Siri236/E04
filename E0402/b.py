text = input("输入：").strip("[]")
new_list = text.split(",")

total = sum(map(int, new_list))

print(total)