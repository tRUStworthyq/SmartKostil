from math import *
from MustHaveFunctional import Normal


#Задание 1
def f1(t):
    t = t * 10 ** -3
    c = 3 * 10 ** -9

    t_p = Normal.norm(t)
    print(t_p)

    r = t / c
    r_p = Normal.norm(r)

    print('R = t / c = ' + t_p + ' / 3 * 10^-9 = ' + r_p)

    return r_p


#Задание 2
def f2(arr):
    #Среднее значение t
    sr = sum(arr) / len(arr)
    sr_p = Normal.norm(sr)
    print('<t> = ' + sr_p)

    print('R0 = 10 кОм')

    C = (sr * 10 ** -3) / 10 ** 4
    C_p = Normal.norm(C)
    print('C = t / R0 = ' + sr_p + ' / 10^4 = ' + C_p)

    Δct = 0.000055
    print('Δc(t) = (10^-4 / 2) * 1.1 = 0.000055')

    Δarr = []
    count = 1
    for i in arr:
        Δarr.append(sr - i)
        print('Δ%d = %g' % (count, sr - i))
        count += 1

    Δcl = sqrt(sum([i ** 2 for i in Δarr]) / 380)
    Δcl_p = Normal.norm(Δcl)
    print('ΔСл = sqrt((Δ1^2 + Δ2^2 + ... + Δ20^2) / 19 * 20) = ' + Δcl_p)

    Δt = sqrt(Δct ** 2 + Δcl ** 2)
    Δt_p = Normal.norm(Δt)
    print('Δt = sqrt(Δc^2 + ΔСл^2) = sqrt(0.000055^2 + ' + Δcl_p + ' = ' + Δt_p)

    ΔC = Δt / 10 ** 7
    ΔC_p = Normal.norm(ΔC)
    print('ΔC = Δt/R0 = ' + Δt_p + ' / 10 ^ 4 = ' + ΔC_p)

    print('C = (' + C_p + ' +- ' + ΔC_p + ') Ф')

    return C_p, ΔC_p, Δcl_p, sr_p




