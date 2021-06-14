'''1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.'''

with open('file.txt', 'a') as f:
    while True:
        text = input()
        if text == '':
            break
        f.write(text + '\n')


'''2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк, 
количества слов в каждой строке.'''

with open('file.txt', 'r') as f:
    lines = f.readlines()
    q_lines = len(lines)
    for text in lines:
        q_word = text.split()
        print(f'{text[:-1]} - {len(q_word)}')

'''3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.'''

workers = {}

with open('zp.txt') as f:
    lines = f.readlines()
    n_people = len(lines)
    total_amount = 0

    for text in lines:
        words = text.split()
        workers[words[0]] = int(words[2])

    for i in workers:
        if workers[i] < 20000:
            print(f'У {i}а зарплата меньше 20т({workers[i]})')
        total_amount += workers[i]

    print(f'Средняя зарплата сотрудников - {total_amount / n_people}')

'''4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.'''

translate = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('qq.txt', 'r') as f_in:
    with open('ww.txt', 'a') as f_out:
        for string in f_in:
            words = string.split()
            for i in range(len(words)):
                if words[i] in translate:
                    words[i] = translate[words[i]]
            f_out.write(' '.join(words) + '\n')

'''5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.'''

with open('file2.txt', 'w') as f:
    f.write('1 2 3 4 5 6 7 8 9')

with open('file2.txt', 'r') as f:
    num = f.read().split()
    summa = 0
    for i in num:
        summa += int(i)
    print(f'Сумма чисел в файле равна - {summa}')

'''6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных, 
практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не обязательно 
были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) 

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}'''

with open('file2.txt', 'r') as f:
    lst_text = f.readlines()
    dct = {}
    for row in lst_text:
        numbers = ''
        lst_word = row.split()
        for word in lst_word:
            w = ''
            for symb in word:
                if symb.isdigit():
                    w += symb

            numbers += w + ' '
        s_num = numbers.split()
        summa = 0
        for i in s_num:
            summa += int(i)
        dct[lst_word[0][:-1]] = summa
    print(dct)

'''7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью. 
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.'''

import os, json

DIR = 'files'
file_to_read_path = os.path.join(DIR, 'task7.txt')
file_to_write_path = os.path.join(DIR, 'task7.json')
result = []
profit = {}
average = []

with open(file_to_read_path, 'r', encoding='utf-8') as file_read:
    counter = 1
    while True:
        line = file_read.readline().split()
        if not line:
            break

        profit[line[0]] = float(line[-2]) - float(line[-1])
        if profit[line[0]] > 0:
            average.append(profit[line[0]])

        counter += 1

result = [profit, {'average_profit': sum(average) / len(average)}]

with open(file_to_write_path, 'w', encoding='utf-8') as file_write:
    json.dump(result, file_write)
