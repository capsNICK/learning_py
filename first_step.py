# Переменная - способ хранения данных в программе.
# Операторы - знаки математических действий.
# Операции - любые действия, которые совершаются с помощью операторов.

#////////////////////////////////////#
#   3. Строки, списки, кортежи и словари
# Строка - фрагмент текста в программе (последовательность символов).

#   Создание строк
#Для создания строки нужно ввести данные в ковычках (одинарные или двойные).
#fred = 'Почему у горилл большие ноздри? Потому что у них большие пальцы!'
#print(fred)
# Чтобы ввести несколько строк текста через Enter используется три одинарные ковычки:
# fred1 = '''Что едят на полдник динозавры?
# ТиРекс-кекс!'''
# print(fred1)

#   Проблемы со строками
# Существуют такие случаи, когда необходимо использовать ковычки для переменной, но возникает синтаксическая ошибка.
# Чтобы такого не возникало используют экранирование при помощи \.  
# single_qoute_str = '"Тут что-то не так, не будь я д\'Артаньян", - подумал он.'
# dowble_qoute_str = "\"Тут что-то не так, не будь я д'Артаньян\", - подумал он."
# print(single_qoute_str)
# print(dowble_qoute_str)
# Лучше использовать ''' ковычки. 

#   Переменные внутри строк
# Подстановка (встраивание значения в строку) - печать строк, содержащие значения переменных при помощи метки %s.
# Например_1:
# myscore = 1000
# message = 'Мой счет: %s очков'
# print(massage % myscore)

# Например_2:
# joke_text = '%s: приспособление для поиска мебели в темноте'
# bodypart1 = 'Коленка'
# bodypart2 = 'Лодыжка'
# print(joke_text % bodypart1)
# print(joke_text % bodypart2)

# Для использования нескольких меток необходимо расположить их в скобках:
# nums = 'Что сказало число %s числу %s? Славный поясок!'
# print(nums % (0, 8))

#     Умножение строк
# print('a' * 10) #десять раз a
# Это может пригодиться для вывода строк с отступом:
# spaces = ' ' * 25
# print('%s Задний переулок 12,' % spaces)
# print('%s Трясогузочья пустошь' % spaces)
# print('%s Западный Всхрапшир' % spaces)
# print()
# print()
# print('Уважаемый Сэр,')
# print()
# print('Хочу сообщить вам, что кое-где на крыше уборной')
# print('недостает кусков черепицы.')
# print('Думаю, прошлой ночью их сдуло внезапным порывом ветра.')
# print()
# print('С почтением')
# print('Мальком Конфузли')

#   Списки
# С помощью списка можно обращаться к его элементам по отдельности.
# Переменная типа списка создается при помощи [''].
# wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
# print(wizard_list[2]) # в [] указывается элемент к которому необходимо обратиться. Счет ведется с 0.

# Чтобы заменить элемент списка необходимо:
# wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
# wizard_list[2] = 'язык улитки'
# print(wizard_list)

# Для отображения части элементов используется :
# wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
# print(wizard_list[2:5])

# В списках можно хранить:
# some_numbers = [1, 2, 5, 10, 20] #числа
# some_string = ['Нож','отточен', 'точен', 'очень'] #строки
# numbers_and_strings = [7, 'раз', 'отпей', 1, 'раз', 'отъешь'] #числа и строки вперемешу

# В списках могут храниться другие списки:
# numbers = [1, 2, 3, 4, 5]
# strings = ['хватит', 'циферки', 'считать']
# mylist = [numbers + strings]
# print(mylist)

#   Добавление элементов в список
# Функция - фрагмент кода, который выполняет какую-то задачу.
# append - добавляет элемент к концу списка.
# wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи']
# wizard_list.append('медвежий коготь')
# wizard_list.append('мандрагора')
# wizard_list.append('болиголов')
# wizard_list.append('болотный газ')
# print(wizard_list)

#   Удаление элементов списка
# Удаление выполняется с помощью команды del.
# wizard_list = ['паучьи лапки', 'жабий палец', 'глаз тритона', 'крыло летучей мыши', 'жир слизня', 'перхоть змеи', 'медвежий коготь', 'мандрагора', 'болиголов', 'болотный газ']
# del wizard_list[5]
# del wizard_list[8]
# del wizard_list[7]
# del wizard_list[6]
# print(wizard_list)

#   Списковая арифметика
# Сложение
# list1 = [1, 2, 3, 4, 5]
# list2 = ['я', 'забрался', 'под', 'кровать']
# print(list1 + list2)

# Результат сложения двух списков можно поместить в другую переменную:
# list1 = [1, 2, 3, 4, 5]
# list2 = ['я', 'забрался', 'под', 'кровать']
# list3 = list1 + list2
# print(list3)

# Умножение
# list1 = [1, 2]
# print(list1 * 5)

# Деление и вычитание для списков не работают!

#   Кортежи
# Список, элементы которого нельзя изменить после создания
# fibs = (1, 2, 3, 4, 5)
# print(fibs[3])

#   Словари
# Словарями называются наборы значений аналогично спискам и кортежам.
# Разница лишь в том, что для элемента словаря соответствуют ключ и связанное с ним значение.
# favorite_sport = {'Ральф Ульямс': 'Футбол', 'Майкл Типпет': 'Баскетбол', 'Эдвард Элгард': 'Бейсбол', 'Ребекка Кларк': 'Нетбол', 'Этель Смит': 'Бадминтон', 'Фрэнк Бридж': 'Регби'} # Для разделения каждой пары "ключ-значение" использовалось двоеточие. Элементы словаря заключены в фигурные скобки.
# print(favorite_sport['Ребекка Кларк'])

# Для удаления удаления значения из словаря используется ключ.
# favorite_sport = {'Ральф Ульямс': 'Футбол', 'Майкл Типпет': 'Баскетбол', 'Эдвард Элгард': 'Бейсбол', 'Ребекка Кларк': 'Нетбол', 'Этель Смит': 'Бадминтон', 'Фрэнк Бридж': 'Регби'} 
# del favorite_sport['Этель Смит']
# print(favorite_sport)

# Ключ служит для замены значения в словаре
# favorite_sport = {'Ральф Ульямс': 'Футбол', 'Майкл Типпет': 'Баскетбол', 'Эдвард Элгард': 'Бейсбол', 'Ребекка Кларк': 'Нетбол', 'Этель Смит': 'Бадминтон', 'Фрэнк Бридж': 'Регби'} 
# favorite_sport['Ральф Ульямс'] = 'Хоккей на льду'
# print(favorite_sport)

#Объеденять словари оператором "+" нелья!

#Упражнения
# 1. 
# games = ['WoD', 'баскетбол']
# foods = ['apple', 'pizza']
# favorites = games + foods
# print(favorites)

# 2.
# house = 3
# ninja = 25
# tunnels = 2
# sumyr = 40
# allwarr = house * ninja + tunnels * sumyr
# print(allwarr)

# 3.
# firstname = 'Alexander'
# lastname = 'Malysh'
# meet = 'Привет, %s %s!'
# print(meet % (firstname, lastname)) 


#////////////////////////////////////#
#   4. Рисование с помощью черепашки
# Упражнения
# 1.
# import turtle
# t = turtle.Pen()
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# 2.
# import turtle
# t = turtle.Pen()
# t.forward(100)
# t.left(120)
# t.forward(100)
# t.left(120)
# t.forward(100)

# 3.
# import turtle
# t = turtle.Pen()
# t.up()
# t.forward(20)
# t.down()
# t.forward(60)
# t.up()
# t.forward(20)
# t.left(90)
# t.up()
# t.forward(20)
# t.down()
# t.forward(60)
# t.up()
# t.forward(20)
# t.left(90)
# t.up()
# t.forward(20)
# t.down()
# t.forward(60)
# t.up()
# t.forward(20)
# t.left(90)
# t.up()
# t.forward(20)
# t.down()
# t.forward(60)
# t.up()
# t.forward(20)
# t.left(90)
