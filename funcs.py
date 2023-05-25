def sum_(a, b):
    return a + b


number_1 = int(input('Enter 1st number: '))
number_2 = int(input('Enter 2nd number: '))

print(f'Сумма {number_1} и {number_2} = {sum_(number_1, number_2)}')


def sub_(c, d):
    return c - d


"""Знаю, что функции пишутся вначале, я для наглядности скриншота так сделал"""

number_3 = int(input('Enter reduced: '))
number_4 = int(input('Enter deductible: '))

print(f'Разность {number_3} и {number_4} = {sub_(number_3, number_4)}')
