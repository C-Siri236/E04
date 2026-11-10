import ast

user_input = input("输入: ")
my_list = ast.literal_eval(user_input)


if len(my_list) == 1:
    result = my_list  
else:
    result = [my_list[0], my_list[-1]] 
print(result)