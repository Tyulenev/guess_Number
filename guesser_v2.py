import random

try_list = []

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []  # Вспомогательный лист более вероятных

#Создание нового листа (list2)
def gen_list_main(try_list:list):
    l2=[]
    for tl1 in try_list:
        if int(tl1.__getitem__(1).__getitem__(0)) > 3:
            for ch1 in tl1.__getitem__(0):
                if not l2.__contains__(ch1):
                    l2.append(ch1)
            break
    #
    #     elif int(tl1.__getitem__(1).__getitem__(0)) > 2:
    #         for ch1 in tl1.__getitem__(0):
    #             if not l2.__contains__(ch1):
    #                 l2.append(ch1)
    #
    #     # Добавляем случ. 1 из этой последовательности
    #     elif int(tl1.__getitem__(1).__getitem__(0)) > 1:
    #         for ch1 in tl1.__getitem__(0):
    #             if not l2.__contains__(ch1):
    #                 l2.append(ch1)
    #                 break

    for tl1 in try_list:
        if int(tl1.__getitem__(1).__getitem__(0)) == 0:
            del_str_from_list(tl1.__getitem__(0), list1)
            del_str_from_list(tl1.__getitem__(0), l2)


    if len(l2) < 4:
        # list2 = list1
        for l in list1:
            l2.append(l)

    return l2

def data_atempt_res_in():
    not_full = input('Введите количество, входящих в ответ, цифр: ')
    full = input('Введите количество, стоящих на своих местах, цифр: ')
    return[not_full, full]


def add_to_try_list(attempt_1:str, result_attempt, list2:list, try_list:list):
    tt=[]
    tt.append(attempt_1)
    tt.append(result_attempt)
    tt.append(list2)
    try_list.append(tt)
    return try_list


def print_try_list(t_l:list):
    i = 1
    for t in t_l:
        print(i, ' - ', t)
        i+=1

def string_equals_by_numbers(s1:str, s2:str):
    l1 = [x for x in s1]
    l2 = [x for x in s2]
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False

def chars_of_string_is_not_in_tryList(s1:str, try_list: list):
    for t_l in try_list:
        if string_equals_by_numbers(t_l.__getitem__(0), s1):
            return False
    return True

def full_string_is_not_in_tryList(s1:str, try_list: list):
    for t_l in try_list:
        if t_l.__getitem__(0) == s1:
            return False
    return True




#Генерация 4-х значного числа из
def generate_str_val(l1: list):
    str_val = ''
    while len(str_val) < 4:
        rand_index = int(random.random() * len(l1))
        #print('rand_index = ', rand_index)
        rand_val = str(l1.__getitem__(rand_index))
        if rand_val not in str_val:
            str_val += rand_val

    return str_val



def del_str_from_list(string1: str, list1: list):  # Удаление строки из списка int
    l_internal = list1
    for l1 in list1:
        if str(l1) in string1:
            print('deliting from main list of elements : ', str(l1))
            l_internal.remove(l1)
    return l_internal

attempt_1 = ''

while True:
    list2 = gen_list_main(try_list)

    if len(list2)>4:
        while True:
            attempt_1 = generate_str_val(list2)
            print(attempt_1)
            if chars_of_string_is_not_in_tryList(attempt_1, try_list): break
    else:
        while True:
            attempt_1 = generate_str_val(list2)
            if full_string_is_not_in_tryList(attempt_1, try_list): break

    print('Попробуйте число - ', attempt_1)
    result_attempt = data_atempt_res_in()
    try_list = add_to_try_list(attempt_1, result_attempt, list2, try_list)
    print_try_list(try_list)