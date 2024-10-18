def chain2D(L):
    return [eachOb for each in L for eachOb in each]
def splitran(L, freq):
    run = True
    tempL = []
    ListA = []
    ListB = []
    n = 0
    for each in L:
        if '\n' in each:
            if each.split('\n') == ['']:
                pass
            else: 
                tempL.append(each.split('\n')[0])
        elif '\n' not in each:
            tempL.append(each)
    for _ in range(tempL.count('')):
        tempL.remove('')
    for each in range(len(tempL)//freq):
        for eachInd in range(freq):
            ListB.append(tempL[eachInd+each*freq])
        ListA.append(ListB)
        ListB = []
    return ListA
DataPaper = open("C:/Users/seunghyeon/Documents/GitHub/python_enhanced/CNNproject/datasets_228_482_diabetes.txt", "r", encoding = "utf8")
splitL = [each.split(',') for each in [DataPaper.readline(each) for each in range(768)]]
#Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
#9
print(splitL)