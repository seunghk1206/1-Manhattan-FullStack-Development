def replace(OriginalPhrase, target, changePhrase):
    splitL = OriginalPhrase.split(target)
    ret = ''
    if len(splitL) != 1:
        for each in range(len(splitL)):
            ret += splitL[each]
            if each == len(splitL)-1:
                pass
            else:
                ret += changePhrase
        return ret
    else:
        return OriginalPhrase

def simpleDerivative(exp):
    splitL = exp.split('x^')
    ret = ''
    for each in splitL:
        try:
            power = int(each)
            ret += str(power)+'x^' + str(power-1)
        except:
            ret += each
    return ret

def powerDerivative(exp):
    splitL = exp.split('^x')

def chainRule(exp):
    splitL = exp.split(')^')
    ret = ''
    retL = []
    if 'sin(x)' in exp:
        splitL = replace(exp, 'sin(x)', 'cos(x)')
        retL.append(splitL)
    if 'cos(x)' in exp:
        splitL = replace(exp, 'cos(x)', '(-sin(x))')
        retL.append(splitL)
    if 'tan(x)' in exp:
        splitL = replace(exp, 'tan(x)', '(sec(x)*sec(x))')
        retL.append(splitL)
    if 'sec(x)' in exp:
        splitL = replace(exp, 'sec(x)', '(sec(x)*tan(x))')
        retL.append(splitL)
    if '^' in exp:
        if 'x^' in exp:
            splitL = simpleDerivative(exp)
            retL.append(splitL)
        if '^x' in exp:
            splitL = powerDerivative(exp)

def Derivative(exp):
    splitL = exp
    retL = []
    ret = ''
    if 'sin(x)' in exp:
        splitL = replace(exp, 'sin(x)', 'cos(x)')
        retL.append(splitL)
    if 'cos(x)' in exp:
        splitL = replace(exp, 'cos(x)', '(-sin(x))')
        retL.append(splitL)
    if 'tan(x)' in exp:
        splitL = replace(exp, 'tan(x)', '(sec(x)*sec(x))')
        retL.append(splitL)
    if 'sec(x)' in exp:
        splitL = replace(exp, 'sec(x)', '(sec(x)*tan(x))')
        retL.append(splitL)
    if '^' in exp:
        if 'x^' in exp:
            splitL = simpleDerivative(exp)
            retL.append(splitL)
        if '^x' in exp:
            splitL = powerDerivative(exp)
    for each in retL:
        ret += each
        if retL.index(each) == len(retL)-1:
            pass
        else:
            ret += '+'
    print(ret)

Derivative('sin(x)sec(x)x^2')