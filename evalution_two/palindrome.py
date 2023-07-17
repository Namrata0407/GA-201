def is_palindrome_number(num):
    num_str = str(num)
    return num_str == num_str[::-1]


print(is_palindrome_number(121))  
print(is_palindrome_number(123))  
