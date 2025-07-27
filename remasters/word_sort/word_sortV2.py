def WordCount():
    shake = open('midsummer.txt')
    count = open('countOutput.txt', 'w')
    words = []
    countL = []
    for line in shake:
        words += line.split()
    for i in words:
        if i in countL:
            continue
        for ii in words:
            if i in countL:
                if countL[countL.index(i)] == ii:
                    countL[countL.index(i) + 1] += 1
            else:
                countL.append(i)
                countL.append(0)
                if countL[countL.index(i)] == ii:
                    countL[countL.index(i) + 1] += 1
    count.write(str(countL))
    shake.close()
    count.close()

WordCount()