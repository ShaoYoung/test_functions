# Задание списка из n чисел последовательности
def get_list(n):
    list_chain = []
    # mystr = list() - альтернативный вариант задания списка
    for i in range(1, n + 1):
        list_chain.append(round((1 + 1 / i) ** i, 2))
    result = 0
    for i in list_chain:
        result += i
    return result

# print(get_list(3))
# 3 -> 6.62
# 5 -> 11.55
# 8 -> 19.19


# слово "конфета" с правильными окончаниями
def ending(n, variant=1):
    if n % 100 in [0, 10, 11, 12, 13, 14]:
        return 'конфет'
    elif n % 10 in [2, 3, 4]:
        return 'конфеты'
    elif n % 10 in [1] and variant:
        return 'конфета'
    elif n % 10 in [1] and not variant:
        return 'конфету'
    elif n % 10 in [0, 5, 6, 7, 8, 9]:
        return 'конфет'

# ending('0')


# поиск недостающего числа по условию A[i] - 1 = A[i-1].
def find_missing_number(number_list):
    for i in range(0, len(number_list)-1):
        if number_list[i]+1 != number_list[i+1]:
            return number_list[i]+1
    return None

# print(find_missing_number([1,2,4]))
