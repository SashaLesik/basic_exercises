# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
list_names = list()
for dicts in students:
    new_name = (dicts['first_name'])
    list_names.append(new_name)

for li in set(list_names):
    list_count = list_names.count(li)
    print(f'{li}:{list_count}')




# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша


from collections import Counter

students_2 = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
list_names = list()
for dicts in students_2:
    new_name = dicts['first_name']
    list_names.append(new_name)
count = Counter(list_names)
count_final = dict(count)
max_val = max(count_final.values())
final_dict = {k: v for k, v in count_final.items() if v == max_val}
print("Самое частое имя среди учеников:")
print(*final_dict)





    
    
    



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
list_names = list()

for index, lists in enumerate(school_students, start=1):
    list_names = list()
    for dicts in lists:
        new_name = dicts['first_name']
        list_names.append(new_name)
    count_st = Counter(list_names)
    count_final = dict(count_st)
    max_val = max(count_final.values())
    final_dict = {k: v for k, v in count_final.items() if v == max_val}
    print(f'Самое частое имя в классе {index}')
    print(*final_dict)
    
            


# Задание 4 и 5 пока не сделала, хочу сделать после твоих комментариев, так как
# , кажется, я чутка усложняю всё или делаю не тем способом, каким было задумано. 
