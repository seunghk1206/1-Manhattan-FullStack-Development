
v = int(input("how many cards? "))
limit = int(input("what would you set as a limit? "))
x = []
l = []
sum = 0
run = 1
if 3 <= v <= 100:
    n = list(input().split(', '))
    if len(n) == v:
        while run == 1:
            if len(x) == 3:
                break
            elif int(max(n)) <= limit:
                for i in range(3):
                    x.append(max(n))
                    n.remove(max(n))
                break
            elif int(max(n)) > limit:
                n.remove(max(n))
        for a in range(len(x)):
            sum += int(x[a])
        print(sum)
    else:
        print("only", v, "cards accepted")
else:
    print("too many cards, error")