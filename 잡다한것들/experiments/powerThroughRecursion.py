# through for loop
def power(num, power):
    a = num
    for _ in range(power-1):
        a *= num
    return a
print(power(5, 3))
# through recursion
def powerRecur(num, power):
    if power == 1:
        return num
    return num * powerRecur(num, power-1)
print(powerRecur(5, 3))