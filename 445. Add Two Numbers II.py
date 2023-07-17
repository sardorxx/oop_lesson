def add_to():
    l1 = [2, 4, 3]
    l2 = [5, 6, 4]
    h = ''
    p = ''
    u = []
    for i in l1:
        b = str(i)
        h += b
    for j in l2:
        k = str(j)
        p += k

    d = int(h)
    q = int(p)
    c = d + q
    m = str(c)
    for e in m:
        r = int(e)
        u.append(r)
    print(u)


add_to()
