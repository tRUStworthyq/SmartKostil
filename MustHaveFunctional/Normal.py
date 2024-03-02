def norm(num):
    k = 0
    while num >= 10 or num < 1:
        if num >= 10:
            k += 1
            num = num / 10
        if num < 1:
            k -= 1
            num = num * 10
    s = ''
    if k == 0:
        s = str(round(num, 2))
    else:
        s = str(round(num, 2)) + ' * 10^' + str(k)
    return s
