def norm(num):
    k = 0
    while num >= 10 or num < 1:
        if num >= 10:
            k += 1
            num = num / 10
        if num < 1:
            k -= 1
            num = num * 10

    return round(num, 2), k

