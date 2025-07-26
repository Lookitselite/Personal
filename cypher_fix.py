def rotate_word(s, n):
    ls = list(s)
    ii = 0
    for i in ls:
        ls[ii] = ord(i)
        ii += 1

    ii = 0
    for i in ls:
        if i >= 97 and i <= 122:
            if i + n >= 97 and i + n <= 122:
                ls[ii] = i + n
            elif i + n > 122:
                d = 122 - i 
                nr = n - abs(d - 1)
                ls[ii] = 97 + nr
            elif i + n < 97:
                d = i - 97
                nr = n + abs(d)
                ls[ii] = 122 + nr
        if i >= 65 and i <= 90:
            if i + n >= 65 and i + n <= 90:
                ls[ii] = i + n
            elif i + n > 90:
                d = 90 - i 
                nr = n - abs(d - 1)
                ls[ii] = 65 + nr
            elif i + n < 65:
                d = i - 65
                nr = n + abs(d)
                ls[ii] = 91 + nr #its the offset, changed from 90->91, fixed. repeat later
        ii += 1
        
    ii = 0
    for i in ls:
        ls[ii] = chr(i)
        ii += 1
    k = ''
    return k.join(ls)