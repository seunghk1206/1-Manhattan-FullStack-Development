def scientificNotation(number):
    if str(type(number)) == "<class 'int'>":
        b = str(number[0])
        b += '.'
        b += str(number[1:])
        b += '*10^'
        b += str(len(number)-1)
        return b
    elif str(type(number)) == "<class 'float'>":
        x = number.split('.')
        for each in number:
            if each != 0:
                n = number[number.index(each):]
                break
        b = str(n[0])
        b += '.'
        b += str(n[1:])
        b += '*10^'
        b += str(-number.count(0))
        return b
    else:
        print('critical error!')
n = 0.1283
scientificNotation(n)
