def count_negative_numbers(num_list):
    try:
        count = 0
        for num in num_list:
            if num < 0:
                count += 1
        return count
    except Exception as e:
        return e
    
a = [10, -1, 2, -3, 4, -5, 1, 3, 3, -5, 6, 7, 8]
print(count_negative_numbers(a))