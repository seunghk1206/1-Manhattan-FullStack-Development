Dict = {}
Ln2 = ['the', 'word']

for eachWord in Ln2:
    try:
        Dict[eachWord][Ln2[Ln2.index(eachWord)+1]] += 1
    except:
        Dict[eachWord][Ln2[Ln2.index(eachWord)+1]] = 1

print(Dict)