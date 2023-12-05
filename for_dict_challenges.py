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
#final_dict = {k: v for k, v in count_final.items() if v == max_val}
#print("Самое частое имя среди учеников:")
#print(*final_dict)
print("Самое частое имя среди учеников:")
for name, counter in count_final.items():
    if counter == max_val:
        print(name)





    
    
    



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
    for name, counter in count_final.items():
        if counter == max_val:
            print(f'Самое частое имя в классе {index}')
            print(name)
    
            


#Задание 4.  Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

for lists in school:
    count_boys = 0  # Вопрос: можно ли здесь использовать enumerate (Если да, то как?)
    count_girls = 0
    for dict in lists["students"]: 
        name = dict['first_name']
        
        if is_male[name] is True:
            count_boys += 1            
        else:
            count_girls += 1
                    
    print(f''' В классе {lists["class"]} мальчики {count_boys},
           девочки {count_girls} ''')
            
            



# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}
# ???
