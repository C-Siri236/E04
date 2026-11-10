# 将整数表示为各位数字的列表，通过列表求整数加1的和
import ast

text = input("输入: ")
digits = ast.literal_eval(text)

for i in range(len(digits) - 1, -1, -1):
    if digits[i] < 9:
        digits[i] += 1
        print(digits)
        break  
    else:
        digits[i] = 0  

else:
    digits.insert(0, 1) 
    print(digits)