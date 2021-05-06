import sympy as sym
import math

def replace(OriginalPhrase, target, changePhrase):
    if target in OriginalPhrase:
        return OriginalPhrase.split(target)[0]+changePhrase+OriginalPhrase.split(target)[1]
    else:
        return OriginalPhrase

def CalcOptimization(DerivationPhrase):
    ret = str(DerivationPhrase)
    if '**' in ret:
        ret = replace(ret, '**', '^')
    if 'log' in ret:
        ret = replace(ret, 'log', 'ln')
    if '*ln(e)' in ret or '/ln(e)':
        ret = replace(ret, '*ln(e)', '')
        ret = replace(ret, '/ln(e)', '')
    return ret

x, e = sym.symbols('x e')
expression = sym.log(x)/sym.log(4)
der1 = sym.diff(expression, x)
der1Rep = CalcOptimization(der1)
print('der1_x : ', der1Rep)