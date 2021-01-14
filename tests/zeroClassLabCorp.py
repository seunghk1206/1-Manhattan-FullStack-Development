def boxOrg(Dictionary):
    answer = []
    tempL = []
    temp2L = []
    for each in Dictionary.keys():
        tempL.append(each.split('_')[0])
    tempL = set(tempL)
    for each in tempL:
        tem = []
        for key, val in Dictionary.items():
            if key.split('_')[0] == each:
                tem.append(val)
        temp2L.append(tem)
    for ind, each in enumerate(tempL):
        tem = []
        for key, val in Dictionary.items():
            if val in temp2L[ind] and key.split('_')[0] == each:
                tem.append([key, val])
        maxi = tem[0][1]
        maxItem = tem[0]
        for each in tem:
            if each[1] > maxi:
                maxi = each[1]
                maxItem = each
        answer.append(maxItem[0])
    return answer

print(boxOrg({"1_Low":3,"1_Mid":5,"119_Low":1,"119_Mid":3,"119_High":7,"126_Mid":7,"126_High":1}))