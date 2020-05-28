import random
import datetime
import time


atempt_number = 1

#Функция создания случайного числа с неповторяющимися цифрами
def getRandomNumber(max_count:int):
    out_val = ''
    number_rand1 = int(random.random()*10)
    while len(out_val)<max_count:
        number_i = str(int(random.random()*10))
        if (out_val.find(number_i)==-1):
            out_val += number_i
    print('Загадываем число ...')
    time.sleep(1)
    print('Число загадано...4-х значное')
    #Запись загаданного значения в файл
    now = datetime.datetime.now()
    f= open('trough_number.txt','a')
    f.write(f'Загаданное число ({now}) - {out_val}.\n')
    f.close
    return int(out_val)



def checkCount(x1:int, user_data_in:int):
    out_list = []
    user_list = []
    check_list = [] #ПРоверка совпадений
    x2 = int(x1)
    correct_number_count = 0
    
    #Создание объекта list элементов числа - out_list
    while x2>0:
        part_of_number = x2%10
        out_list.insert(0, part_of_number)
        x2=int(x2/10)

    x_user = int(user_data_in)
    while x_user>0:
        part_of_number = x_user%10
        user_list.insert(0, part_of_number)
        x_user=int(x_user/10)

    if len(user_list)!=len(out_list): 
        print('Неправильная длинна числа в последней попытке')
        return False

    #ПРоверка введенного и загаданного
    for check_index in range(len(out_list)):
        if user_list.__getitem__(check_index) == out_list.__getitem__(check_index):
            check_list.insert(0,1)
        else:
            check_list.insert(0,0)

    for c in check_list:
        if c==1: correct_number_count+=1
    print('Количество полных совпадений (на своих местах) : ', correct_number_count)
    if (user_list == out_list): print('Ура! Вы угадали!!! \nКоличество попыток:', atempt_number)
    
    #Создание нового листа без дубликатов в вводе
    list_in_without_repeated_element = []
    count_repeated_element = 0          # Количество элементов, которое повторяется в вводе пользователя и загаданном числе
    list_in_without_repeated_element = list(set(user_list))
    #print(list_in_without_repeated_element)
    #Вхождение цифр в загаданное число
    for fig in list_in_without_repeated_element:
        if fig in out_list: count_repeated_element+=1
    print(f'Общее количество, совпадающих элементов: {count_repeated_element}')
    
    
    return (user_list == out_list)



x_number = getRandomNumber(4)

check_res_bool = 0
stop_game = 1
number_of_attemps = int(input('Введите количество попыток '))
while (stop_game):
    print(f'\nПопытка №{atempt_number}')
    in_data = input('Введите число: ')
    check_res_bool = checkCount(x_number,in_data)
    if not atempt_number < number_of_attemps:
        
        print('Число не угадано за указанное количество попыток! \nЗагаданное число было: ',x_number)
        #break

    atempt_number += 1
    if check_res_bool or atempt_number>number_of_attemps:
        stop_game = input('Хотите повторить игру? (1-да, 0-нет) : ')
        if int(stop_game)==1:
            x_number = getRandomNumber(4)
            check_res_bool = 0
            atempt_number = 1
        else:
            break

