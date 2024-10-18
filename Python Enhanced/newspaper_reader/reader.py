import itertools
paper = open("./newspaper_reader/eng_news_2016_10K-sentences.txt", "r", encoding = "utf8")
# "r", UTF-8,, ./newspaper_reader/eng_news_2016_10K-sentences.txt
Dict = {}
Lolines = []
tempL = []
Ln2 = []
#dict
def replace(listAccept, listRecieve, whichOne):
    for each in listAccept:
        listRecieve.append(each.split(whichOne))
    listAccept.clear()
    dummy = list(itertools.chain(*listRecieve))
    listRecieve.clear()
    for i in dummy:
        listRecieve.append(i)
for i in range(10000):
    lines = paper.readline(i)
    Lolines.append(lines)
replace(Lolines, tempL, '\t')
replace(tempL, Lolines, '\n')
replace(Lolines, tempL, ',')
replace(tempL, Lolines, '.')
replace(Lolines, tempL, '-')
replace(tempL, Lolines, ':')
replace(Lolines, tempL, ';')
replace(tempL, Lolines, '1')
replace(Lolines, tempL, '2')
replace(tempL, Lolines, '3')
replace(Lolines, tempL, '4')
replace(tempL, Lolines, '5')
replace(Lolines, tempL, '6')
replace(tempL, Lolines, '7')
replace(Lolines, tempL, '8')
replace(tempL, Lolines, '9')
replace(Lolines, tempL, ')')
replace(tempL, Lolines, '(')
replace(Lolines, tempL, '@')
replace(tempL, Lolines, '"')
replace(Lolines, tempL, "'")
replace(tempL, Lolines, '~')
replace(Lolines, tempL, '`')
replace(tempL, Lolines, '?')
for each in range(len(Lolines)):
    Ln = list(Lolines[each].split(" "))
    for each in Ln:
        Ln2.append(each.lower())
for eachWord in Ln2:
    try:
        Dict[eachWord] += 1
    except:
        Dict[eachWord] = 1
print(Dict)