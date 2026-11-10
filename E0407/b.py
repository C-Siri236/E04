# 将整数表示为各位数字的列表，通过列表求两个整数的和。例如[1, 2, 3] + [4, 5, 6] 
# = [5, 7, 9]，[9, 2, 7] + [1, 3, 5] = [1, 0, 6, 2]。
import ast

def add_lists(list1, list2):
    result = []
    i, j = len(list1) - 1, len(list2) - 1
    carry = 0  # 进位
    
    # 只要还有数字没算完，或者还有进位没处理，就继续循环
    while i >= 0 or j >= 0 or carry > 0:
        # 如果指针越界了，就当作0处理
        num1 = list1[i] if i >= 0 else 0
        num2 = list2[j] if j >= 0 else 0
        
        total = num1 + num2 + carry
        
        # 当前位保留个位，进位算给下一位
        result.insert(0, total % 10) 
        carry = total // 10
        
        i -= 1
        j -= 1
        
    return result

# 接收输入
text1 = input("输入列表1: ")
list1 = ast.literal_eval(text1)
text2 = input("输入列表2: ")
list2 = ast.literal_eval(text2)

print(add_lists(list1, list2))