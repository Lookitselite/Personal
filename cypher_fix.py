def rotate_word(word, rotations):
    ls = list(word)
    ii = 0
    for i in ls:
        ls[ii] = ord(i)
        ii += 1

    ii = 0
    for i in ls:
        if i >= 97 and i <= 122:
            if i + rotations >= 97 and i + rotations <= 122:
                ls[ii] = i + rotations
            elif i + rotations > 122:
                d = 122 - i 
                nr = rotations - abs(d - 1)
                ls[ii] = 97 + nr
            elif i + rotations < 97:
                d = i - 97
                nr = rotations + abs(d)
                ls[ii] = 122 + nr
        if i >= 65 and i <= 90:
            if i + rotations >= 65 and i + rotations <= 90:
                ls[ii] = i + rotations
            elif i + rotations > 90:
                d = 90 - i 
                nr = rotations - abs(d - 1)
                ls[ii] = 65 + nr
            elif i + rotations < 65:
                d = i - 65
                nr = rotations + abs(d)
                ls[ii] = 91 + nr #its the offset, changed from 90->91, fixed. repeat later
        ii += 1
        
    ii = 0
    for i in ls:
        ls[ii] = chr(i)
        ii += 1
    k = ''
    return k.join(ls)

allTestsCorrect = True
print(ord('X'))
print(rotate_word('XYZ', 3))
correct = rotate_word('bob', 3) == 'ere'
if not correct:
    print('Error in rotate_word()!')
allTestsCorrect = allTestsCorrect and correct
    
correct = rotate_word('BOB', 3) == 'ERE'
if not correct:
    print('Error in rotate_word()!')
allTestsCorrect = allTestsCorrect and correct