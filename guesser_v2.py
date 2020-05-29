import random

try_list = []

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []  # Вспомогательный лист более вероятных




#Генерация 4-х значного числа из
def generate_tsk(l1: list):
    str_val = ''
    while len(str_val) < 4:
        rand_index = int(random.random() * len(l1))
        print('rand_index = ', rand_index)
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


while True:
    print(generate_tsk(list1))
    input()