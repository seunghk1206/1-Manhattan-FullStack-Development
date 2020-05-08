a= int(input("How many vocabs required? "))
length = []
len2 = []
words = []
for i in range(a):
    inputx = input()
    length.append(len(inputx))
    words.append(inputx)
for each in range(len(length)):
    len2.append(length[each])
print(len2)
for i in range(len(length)):
    for x in range(len(len2)):
        if length[i] == len2[x]:
            if words[len2.index(len2[x])] > words[length.index(length[i])] or words[length.index(length[i])] > words[len2.index(len2[x])]:
                words[len2.index(len2[x])], words[length.index(length[i])] = words[len2.index(len2[x])], words[length.index(length[i])]
            else:
                pass
for m in range(len(length)):
    minLn = length.index(min(length))
    print(words[minLn])
    length.remove(min(length))
    words.remove(words[minLn])