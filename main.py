text = ' Домашнее задание к лекции 8 '
print(text.center(50, "%"))
text = ' Задание 1-3 '
print(text.center(50))

from pprint import pprint

#Задача 1

def creation_cook_book(file_txt):
    with open(file_txt, encoding='utf-8') as f:
        book = {}
        for l in f.read().split('\n\n'):
            key = (l.split('\n',2))[0]
            v = ((l.split('\n',2))[2]).split('\n')
            d = []
            for v2 in v:
                v3 = v2.split(' | ')
                d.append({'ingredient_name': v3[0],'quantity': int(v3[1]),'measure': v3[2]})
            book[key]=d
    return book

#Задача 2

def shop_list(cook_book, dishes, number_person):
    total = {}
    for dish in dishes:
        if dish in cook_book:
            for values in cook_book[dish]:
                if values['ingredient_name'] in total:
                    total[values['ingredient_name']]['quantity'] += values['quantity']*number_person
                else: 
                    total[values['ingredient_name']] = {'measure':values['measure'], 'quantity':(values['quantity']*number_person)}
        else: 
            print(f'Блюда {dish} нет в списке')    
    return total

#Задача 3

#Считаем количествор строк в файле
def sum_lines_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return sum(1 for _ in f)

names = ['1.txt', '2.txt', '3.txt']

#Сортируем список имен файлов, записываем их в файл в сообветствии с количеством строк
def file_creation(names_files, write_file):
    file = []
    sort_sum = {}
    sum_sort = {}
    for i in names_files:
        j = sum_lines_file(i)
        sort_sum[j] = i
        sum_sort[i] = j
    sort_ = [x[1] for x in sorted(sort_sum.items())]
    for i in sort_:
        file.append(i)
        file.append(str(sum_sort[i]))
        with open(i, 'r', encoding='utf-8') as r:
            for l in r.read().split('\n'):
                file.append(l)
    file_n = '\n'.join(file)
    with open(write_file, 'w', encoding='utf-8') as w:
        w.writelines(file_n)
    return sum_sort

#Итог
print('Задача 1')
print()
pprint(creation_cook_book('recipes.txt'))
print()
print('Задача 2')
print()
pprint(shop_list(creation_cook_book('recipes.txt'),['Омлет','Фахитос','Салат "Оливье"'], 3))
print()
print('Задача 3')
print()
file_creation(names, '123.txt')
print()
#print(sum_lines_file('recipes.txt'))