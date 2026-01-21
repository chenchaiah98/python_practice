# def larger_numer(num1,num2,larger_num):
#     if larger_num > num1 and larger_num > num2:
#         return larger_num
#     if num1 > num2:
#         return num1
#     else:
#         return num2
    

# a = [10, 20, 100, 30, 40, 50, 100, 300, 600, 700, 800]
# larger_number = 0
# for i in range(len(a)-1):
#     larger_number = larger_numer(a[i],a[i+1],larger_number)
# print(larger_number)


def larger_number(list):
    larger_number = float('-inf')
    for i in list:
        if i > larger_number:
            larger_number = i
    return larger_number

a = [10, 20, 100, 30, 40, 50, 1000, 300, 600, 700, 800]
print(larger_number(a))