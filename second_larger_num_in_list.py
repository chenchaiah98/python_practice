def second_larger_num(num_list):
    if len(num_list) > 1:
        try:
            first_num = second_num = float('-inf')
            for i in range(len(num_list)):
                if num_list[i] > first_num:
                    second_num = first_num
                    first_num = num_list[i]
                elif first_num > num_list[i] > second_num:
                    second_num = num_list[i]
            return second_num
        except Exception as e:
            return e
    else:
        return "List must contain at least two distinct numbers."
    
a = [10, 20, 100, 30, 40, 50, 1000, 300, 600,3000, 700, 800]
a=['wr','wer','as','asdasd']

print(second_larger_num(a)) 