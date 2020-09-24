def AnnualSigma(num, rate, investment):
    if num == 1:
        return investment
    return rate*AnnualSigma(num-1, rate, investment) + investment
print(AnnualSigma(float(input()), 1.06, 2000))
def BankInvestment(num, rate, investment):
    if num == 1:
        return investment
    return rate*AnnualSigma(num-1, rate, investment)
print(BankInvestment(float(input()), 1.06, 2000))