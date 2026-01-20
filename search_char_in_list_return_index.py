def search_char_in_list(char, char_list):
    try:
        for i in range(len(char_list)):
            if char_list[i] == char:
                return i
    except Exception as e:
        return e
    return -1

a = ['a', 'b', 'c', 'd']
print(search_char_in_list('d', a))
print(search_char_in_list('e', a))