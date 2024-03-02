from Labs.Fizika.Sem2 import l2_15, l2_22

if __name__ == '__main__':
    print('Введите номер лабораторной работы:')
    k = input()

    match k:
        case '2_15':
            print('Рассчетная часть')
            print('Задание 1')
            t = float(input('Введите t: '))
            R = l2_15.f1(t)

            print('Задание 2')
            print('Введите 20 значений в строчку через пробел')
            arr = list(map(float, input().split(' ')))
            C1, ΔC, Δcl, sr = l2_15.f2(arr)

            print('Вывод: ')
            print('Результат: ')
            print('№1: R = %g * 10^%d' % (R[0], R[1]))
            print('№2:  <t> = %g * 10^%d (мс)' % (sr[0], sr[1]))
            print('     Δc(t) = 0.000055 (с)')
            print('     ΔСл = %g * 10^%d (мс)' % (Δcl[0], Δcl[1]))
            print('     ΔC = %g * 10^%d (Ф)' % (ΔC[0], ΔC[1]))
            print('     C = (%g * 10^%d +- %g * 10^%d) Ф' % (round(C1[0], 2), C1[1], round(ΔC[0], 2), ΔC[1]))
        case '2_22':
            print('Рассчетная часть')
            print('Задание 1')
            # y = list(map(int, input('Введите 2 значения частоты в Гц в строчку через пробел: ').split(' ')))
            # ΔU1 = list(map(int, input('Введите 2 значения ΔU1 в В в строчку через пробел: ').split(' ')))
            # ΔU2 = list(map(int, input('Введите 2 значения ΔU2 в мВ в строчку через пробел: ').split(' ')))
            y = [2770, 2604]
            ΔU1 = [15, 13]
            ΔU2 = [128, 148]

            C1, C0_1, C_sr1 = l2_22.f1(y, ΔU1, ΔU2)

            print('Задание 2')

            # y = list(map(int, input('Введите 2 значения частоты в Гц в строчку через пробел: ').split(' ')))
            # ΔU1 = list(map(int, input('Введите 2 значения ΔU1 в В в строчку через пробел: ').split(' ')))
            # ΔU2 = list(map(int, input('Введите 2 значения ΔU2 в мВ в строчку через пробел: ').split(' ')))
            # d = list(map(float, input('Введите 6 значений d в мм в строчку через пробел: ').split(' ')))

            y = [2780, 2604]
            ΔU1 = [15, 13]
            ΔU2 = [160, 208]
            d = [4.00, 3.45, 3.55, 3.70, 3.80, 4.00]


            C2, E, C0_2, C_sr2 = l2_22.f2(y, ΔU1, ΔU2, d)


            print('Вывод: ')
            print('Результаты: ')
            print('№1')

            for i in C1:
                print('C = %g * 10^%d' % (i[0], i[1]))
            print('C0 = ' + C0_1)
            print('С ср = %g * 10^%d' % (C_sr1[0], C_sr1[1]))

            print('№2')
            for i in C2:
                print('C = %g * 10^%d' % (i[0], i[1]))
            for i in E:
                print('E = %g * 10^%d' % (i[0], i[1]))
            print('C0 = %g * 10^%d' % (C0_2[0], C0_2[1]))
            print('C cp = %g * 10^%d' % (C_sr2[0], C_sr2[1]))