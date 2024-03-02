from math import *
from MustHaveFunctional import Normal


#Задание 1
def f1(t):
    t = t * 10 ** -3
    c = 3 * 10 ** -9

    t_p = Normal.norm(t)

    r = t / c
    r_p = Normal.norm(r)

    print('R = t / c = %g * 10^%d / 3 * 10^-9 = %g * 10^%d' % (t_p[0], t_p[1], r_p[0], r_p[1]))

    return r_p


#Задание 2
def f2(arr):
    #Среднее значение t
    sr = sum(arr) / len(arr)
    sr_p = Normal.norm(sr)
    print('<t> = %g * 10^%d' % (sr_p[0], sr_p[1]))

    print('R0 = 10 кОм')

    C = (sr * 10 ** -3) / 10 ** 4
    C_p = Normal.norm(C)
    print('C = t / R0 = (%g * 10^%d) / 10^4 = %g * 10^%d' % (sr_p[0], sr_p[1], C_p[0], C_p[1]))

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
    print('ΔСл = sqrt((Δ1^2 + Δ2^2 + ... + Δ20^2) / 19 * 20) = %g * 10^%d' % (Δcl_p[0], Δcl_p[1]))

    Δt = sqrt(Δct ** 2 + Δcl ** 2)
    Δt_p = Normal.norm(Δt)
    print('Δt = sqrt(Δc^2 + ΔСл^2) = sqrt(0.000055^2 + (%g * 10^%d)^2) = %g * 10^%d' % (Δcl_p[0], Δcl_p[1], Δt_p[0], Δt_p[1]))

    ΔC = Δt / 10 ** 7
    ΔC_p = Normal.norm(ΔC)
    print('ΔC = Δt/R0 = (%g * 10^%d) / 10 ^ 4 = %g * 10^%d' % (Δt_p[0], Δt_p[1], ΔC_p[0], ΔC_p[1]))

    print('C = (%g * 10^%d +- %g * 10^%d) Ф' % (C_p[0], C_p[1], ΔC_p[0], ΔC_p[1]))


    return C_p, ΔC_p, Δcl_p, sr_p




