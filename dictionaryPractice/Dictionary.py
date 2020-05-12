##Data structure

#List = 나중에 변화 가능 한 -> 값을 추가하거나 뺄수 있다. -> []
#Tuple = 한 번 만들면나중에 변화가 안됨 -> 값의 변화를 못 줌 -> ()
#Dictionary = List 또는 Tuple에 이름을 지어줘서 관리하는 것. -> {}

my_dict = {} #중괄호는 딕셔너리 호출! 

my_dict['Spring'] = '봄' ##대괄호는 KEY, 이름을 뜻함
my_dict['summer'] = '여름'
my_dict['winter'] = '겨울'
my_dict['Autumn'] = '여름'
print(my_dict)
print(my_dict['Autumn'])

del my_dict['Autumn']


# Key : value      <<key를 통해서 value의 값을 얻을 수 있다는 장점. 
# Spring : 봄     <<이형식이 바로 dictionary 형식

# Summer : 여름
# Winter : 겨울
#{'Spring': '봄', 'summer': '여름', 'winter': '겨울'}

list2 = [[1, 5], [2, 4], [3,5]] 
dictionary = {}
multiply = 0

for eachNum in list2:
    multiply = eachNum[1]* eachNum[0]
    my_dict[multiply] = eachNum
    
print(my_dict)


    

#  [[1, 5], [2, 4], [3,5]] 
#  { : [1, 5], 8 : [2, 4], 15: [3, 5]}