from Labs.Fizika.Sem2 import l2_15

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
            C, ΔC, Δcl, sr = l2_15.f2(arr)

            print('Вывод: ')
            print('Результат: ')
            print('№1: R = %g * 10^%d' % (R[0], R[1]))
            print('№2:  <t> = %g * 10^%d (мс)' % (sr[0], sr[1]))
            print('     Δc(t) = 0.000055 (с)')
            print('     ΔСл = %g * 10^%d (мс)' % (Δcl[0], Δcl[1]))
            print('     ΔC = %g * 10^%d (Ф)' % (ΔC[0], ΔC[1]))
            print('     C = (%g * 10^%d +- %g * 10^%d) Ф' % (round(C[0], 2), C[1], round(ΔC[0], 2), ΔC[1]))





