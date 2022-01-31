# 1.Сформировать строку, в которой содержится информация определенном слове в строке.
# Например "The [номер] symbol in [тут слово] is [значение символа по номеру в слове]".
# Слово и номер получите с помощью input() или воспользуйтесь константой.
# Например (если слово - "Python" а символ 3) - "The 3 symbol in "Python" is t".


word = str(input('Введите слово: '))
length = int(len(word))
number = int(input('Введите номер символа: '))
if number <=  length:
    symb = word[number - 1]
    print('Под номером', number, 'находится символ', symb )
else:
    print('Длина вашего слова меньше заданного числа')

#через try , except немного не вышло


# 2.Ввести из консоли строку.
# Определить количество слов в этой строке, которые заканчиваются на букву "o"
# (учтите, что буквы бывают заглавными).

my_str = str(input('Введите текст: '))

length1 = int(len(my_str))
counter = 0
counter1 = 0

for i in my_str:
    counter1 += 1
    if i == ' ':
        if my_str[counter1-2] == 'о':
            counter += 1
        elif my_str[counter1-2] == 'О':
            counter += 1

if my_str[-1] == 'о':
    counter += 1
elif my_str[-1] == 'О':
    counter += 1

if counter != 0:
    print('В вашем тексте', counter, 'слов, заканчивающихся на о')
else:
    print('В вашем тексте нет слов, заканчивающихся на о')

print('Длина строки - ', len(my_str))
print('Кол-во букв о - ', my_str.count('о'))



# 3.Есть list с данными lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишите механизм, который cформирует новый list (например lst2),
# который содержит только переменные типа str, которые есть в lst1.


lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = lst1.copy()

for i in lst2:
    if type(i) == str:
        print(i)

