"""Rock paper scissors game"""

"""Игра камень ножницы бумага"""

from random import randint
from time import sleep
import sys

st = '_'
st1 = ' '
# КОЛИЧЕСТВО ЦИКЛОВ ИГРЫ ДО ВОЗМОЖНОГО ВЫХОДА
N = 5


def main():
    Nkom = 0
    Nigr = 0
    t = 'None'
    print()
    print('******** Игра с компьютером "Камень, Ножницы, Бумага" *******')
    while t != 'в':
        n1 = 0
        while n1 != N:
            while True:
                i = input('Выберите: <(К)амень>  <(Н)ожницы>  <(Б)умага>  : ')
                i = i.replace(' ', '')
                i = i.lower()
                if i.isalpha():
                    if len(i) == 1:
                        if i == 'к' or i == 'н' or i == 'б':
                            break
                        else:
                            print()
                            print('Ошибка ввода! Введите корректные буквы.')
                    else:
                        print()
                        print('Ошибка ввода! Допустима только одна буква.')
                elif i == '':
                    print()
                    print('Ошибка ввода! Сделайте свой выбор.')
                elif i.isdigit():
                    print()
                    print('Ошибка ввода! Цифры не допустимы.')
                elif len(i) > 1:
                    print()
                    print('Ошибка ввода! Допустима только одна буква.')
                else:
                    print()
                    print('Ошибка ввода! Повторите ввод.')
            n1 += 1
            sleep(0.5)
            print('Раз.........', end='\t')
            sleep(0.5)
            print('Два.........', end='\t')
            sleep(0.5)
            print('Три.........', end='\t')
            sleep(0.5)
            print('\n')
            print(50 * st)
            dc = {'к': 'камень', 'н': 'ножницы', 'б': 'бумага'}
            ls = ["камень", "ножницы", "бумага"]
            n = randint(0, 2)
            kom = ls[n]
            igr = dc[i]
            if kom == igr:
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(18*st1 + '*** Ничья! ***')
                print(12*st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)
            elif kom == 'камень' and igr == 'ножницы':
                Nkom += 1
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(9*st1 + '*** Упссс.... Вы проиграли! ***')
                print(12*st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)
            elif kom == 'ножницы' and igr == 'бумага':
                Nkom += 1
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(9*st1 + '*** Упссс.... Вы проиграли! ***')
                print(12*st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)
            elif kom == 'бумага' and igr == 'камень':
                Nkom += 1
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(9*st1 + '*** Упссс.... Вы проиграли! ***')
                print(12*st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)

            elif kom == 'бумага' and igr == 'ножницы':
                Nigr += 1
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(15*st1 + '*** Вы выиграли! ***')
                print(12*st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)
            elif kom == 'ножницы' and igr == 'камень':
                Nigr += 1
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(15*st1 + '*** Вы выиграли! ***')
                print(12 * st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)
            elif kom == 'камень' and igr == 'бумага':
                Nigr += 1
                print('n =', n1)
                print(7*st1 + f'КОМПЬЮТЕР <{kom}> : <{igr}> ИГРОК')
                print(15*st1 + '*** Вы выиграли! ***')
                print(12 * st1 + f'компьютер <{Nkom}> : <{Nigr}>  игрок')
                print(50 * st)
        while True:
            t = input('ПРОДОЛЖИТЬ ИГРУ..........: <любая буква> , выйти <в>: ')
            t = t.replace(' ', '')
            t = t.lower()
            if t == 'в':
                print()
                print('******** Программа "Камень, Ножницы, '
                      'Бумага": ЗАКРЫТА *******')
                sys.exit()
            elif t.isalpha():
                if len(t) == 1:
                    if t != 'в':
                        break
                else:
                    print()
                    print('Ошибка ввода! Не более одной буквы.')
            elif t.isdigit():
                print()
                print('Ошибка ввода! Цифры не допустимы.')
            else:
                print()
                print('Ошибка ввода! Повторите ввод.')


if __name__ == '__main__':
    main()