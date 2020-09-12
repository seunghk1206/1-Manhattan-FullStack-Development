def scientificNotation(number):
    try:
        number = int(number)
    except:
        number = float(number)
    count = 0 
    a = ''
    print(str(type(number)))
    if str(type(number)) == "<class 'float'>":
        intP = str(eval(str(number))).split('.')[0]
        if intP[0] == '-':
            if len(intP) > 2:
                count = len(intP) - 2
                a += '-'
                a += str(intP[1])
                a += '.'
                a += str(intP[2:])
                a += str(str(number).split('.')[1])
                a += ' * 10^'
                a += str(count)
            else:
                if intP[1] == '0':
                    run = True
                    while run:
                        count += 1
                        number *= 10
                        if int(str(number)[1]) == 0:
                            pass
                        else:
                            break
                    a += str(number)
                    a += ' * 10^(-'
                    a += str(count)
                    a += ')'
                else:
                    return str(number)
        else:
            if len(intP) > 1:
                count = len(intP) - 1
                a += str(intP[0])
                a += '.'
                a += str(intP[1:])
                a += str(str(number).split('.')[1])
                a += ' * 10^'
                a += str(count)
            else:
                if intP == '0':
                    run = True
                    while run:
                        count += 1
                        number *= 10
                        if str(number)[0] == 0:
                            pass
                        else:
                            break
                    a += str(number)
                    a += ' * 10^(-'
                    a += str(count)
                    a += ')'
                else:
                    return str(number)
    elif str(type(number)) == "<class 'int'>":
        if str(number)[0] == '-':
            num = float(str(number)[1:])
            run  = True
            while run:
                count += 1
                num /= 10
                if len(str(num).split('.')[0]) == 1:
                    break
                else:
                    pass
            a += '-'
            a += str(num)
            a += ' * 10^'
            a += str(count)
        elif str(number)[0] != '-':
            num = float(eval(str(number)))
            run  = True
            while run:
                count += 1
                num /= 10
                if len(str(num).split('.')[0]) == 1:
                    break
                else:
                    pass
            a += str(num)
            a += ' * 10^'
            a += str(count)
    return a
n = input("give an input ")
print(scientificNotation(n))