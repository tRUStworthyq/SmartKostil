from MustHaveFunctional import Normal

R = 3.3 * 10 ** 3
#Задание 1
def f1(y, U1, U2):

    print('R = 3.3 * 10^3')

    print('1) Пилообразный сигнал')
    print('2) Гармонический сигнал')
    arr = []

    C1 = 1 / (4 * y[0] * R) * ((U2[0] * 10 ** -3) / U1[0])

    C1_p = Normal.norm(C1)
    arr.append(C1_p)
    y_p1 = Normal.norm(y[0])
    U1_p1 = Normal.norm(U1[0])
    U2_p1 = Normal.norm(U2[0])


    print('1)C = 1 / 4yR * (ΔU2/ΔU1) = (1 / 4 * %g * 10^%d * 3.3 * 10^3) * (%g * 10^%d * 10^-3 / %g * 10 ^%d) = %g * 10^%d' % (y_p1[0], y_p1[1], U2_p1[0], U2_p1[1], U1_p1[0], U1_p1[1], C1_p[0], C1_p[1]))


    C2 = (1 / (2 * 3.14 * y[1] * R)) * (U2[1] * 10 ** -3 / U1[1])

    C2_p = Normal.norm(C2)
    arr.append(C2_p)
    y_p2 = Normal.norm(y[1])
    U1_p2 = Normal.norm(U1[1])
    U2_p2 = Normal.norm(U2[1])

    print('2)C = 1 / 2"PI"yR * (ΔU2/ΔU1) = (1 / 2 * 3.14 * %g * 10^%d * 3.3 * 10^3) * (%g * 10^%d * 10^-3 / %g * 10 ^%d) = %g * 10^%d' % (y_p1[0], y_p1[1], U2_p1[0], U2_p1[1], U1_p1[0], U1_p1[1], C1_p[0], C1_p[1]))

    C_sr = (C1 + C2) / 2
    C_sr_p = Normal.norm(C_sr)
    print('Сср = %g * 10^%d + %g * 10^%d / 2 = %g * 10^%d' % (C1_p[0], C1_p[1], C2_p[0], C2_p[1], C_sr_p[0], C_sr_p[1]))


    print('C0 = 99.12 * 10^-12')
    return arr, '99.12 * 10^-12', C_sr_p

#Задание 2
def f2(y, U1, U2, d):
    sr = sum(d) / len(d)
    sr_p = Normal.norm(sr)

    print('<d> = %g * 10^%d' % (sr_p[0], sr_p[1]))

    print('R = 3.3 * 10^3')

    arr = []

    C1 = 1 / (4 * y[0] * R) * ((U2[0] * 10 ** -3) / U1[0])

    C1_p = Normal.norm(C1)
    arr.append(C1_p)
    y_p1 = Normal.norm(y[0])
    U1_p1 = Normal.norm(U1[0])
    U2_p1 = Normal.norm(U2[0])

    print(
        '1)C = 1 / 4yR * (ΔU2/ΔU1) = (1 / 4 * %g * 10^%d * 3.3 * 10^3) * (%g * 10^%d * 10^-3 / %g * 10 ^%d) = %g * 10^%d' % (
        y_p1[0], y_p1[1], U2_p1[0], U2_p1[1], U1_p1[0], U1_p1[1], C1_p[0], C1_p[1]))

    C2 = (1 / (2 * 3.14 * y[1] * R)) * (U2[1] * 10 ** -3 / U1[1])


    C2_p = Normal.norm(C2)
    arr.append(C2_p)
    y_p2 = Normal.norm(y[1])
    U1_p2 = Normal.norm(U1[1])
    U2_p2 = Normal.norm(U2[1])

    print(
        '2)C = 1 / 2"PI"yR * (ΔU2/ΔU1) = (1 / 2 * 3.14 * %g * 10^%d * 3.3 * 10^3) * (%g * 10^%d * 10^-3 / %g * 10 ^%d) = %g * 10^%d' % (
        y_p2[0], y_p2[1], U2_p2[0], U2_p2[1], U1_p2[0], U1_p2[1], C2_p[0], C2_p[1]))

    print('S = 0.0224 м^2')
    arr2 = []
    E1 = C1 * sr * 10 ** -3 / (8.85 * 10 ** -12 * 0.0224)
    E1_p1 = Normal.norm(E1)
    arr2.append(E1_p1)
    print('1)E = C * d / E0 * S = %g * 10^%d * %g * 10^%d / 8.85 * 10^-12 * 0.0224 = %g * 10^%d' % (C1_p[0], C1_p[1], sr_p[0], sr_p[1], E1_p1[0], E1_p1[1]))

    E2 = C2 * sr * 10 ** -3/ (8.85 * 10 ** -12 * 0.0224)
    E2_p2 = Normal.norm(E2)
    arr2.append(E2_p2)
    print('2)E = C * d / E0 * S = %g * 10^%d * %g * 10^%d / 8.85 * 10^-12 * 0.0224 = %g * 10^%d' % (C2_p[0], C2_p[1], sr_p[0], sr_p[1], E2_p2[0], E2_p2[1]))

    if E1 > E2:
        C0 = (E1 * 8.85 * 10 ** -12 * 0.0224) / sr
        C0_p = Normal.norm(C0)

        print('C0 = E * E0 * S / d = %g * 10^%d * 8.85 * 10^-12 * 0.0224 / %g * 10^%d = %g * 10^%d' % (E1_p1[0], E1_p1[1], sr_p[0], sr_p[1], C0_p[0], C0_p[1]))
    else:
        C0 = (E2 * 8.85 * 10 ** -12 * 0.0224) / sr
        C0_p = Normal.norm(C0)

        print('C0 = E * E0 * S / d = %g * 10^%d * 8.85 * 10^-12 * 0.0224 / %g * 10^%d = %g * 10^%d' % (
        E2_p2[0], E2_p2[1], sr_p[0], sr_p[1], C0_p[0], C0_p[1]))

    C_sr = (C1 + C2) / 2
    C_sr_p = Normal.norm(C_sr)

    print('C cp = %g * 10^%d + %g * 10^%d / 2 = %g * 10^%d' % (C1_p[0], C1_p[1], C2_p[0], C2_p[1], C_sr_p[0], C_sr_p[1]))

    return arr, arr2, C0_p, C_sr_p