def num_of_digits(num:int):
    num = str(num)
    return len(num)


print(num_of_digits(1000)) #➞ 4

print(num_of_digits(12)) #➞ 2

print(num_of_digits(1305981031)) #➞ 10

print(num_of_digits(0)) #➞ 1