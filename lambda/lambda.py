"""
람다는 익명의 함수이다

1. 간결
2. 사람의 언어와 비슷함
3. 다른 언어(자바)에도 있음
"""

#list of strings가정
txt = ["Kim Youngho", "Kim Seunghyeon", "Lee Youngho", "Ju Youngho"]
# kim 을 가진 string 으로 나열하라
#output = [(True, Kim Youngho), (True, Kim Seunghyeon), (), ()]
prac = map(lambda s:(True, s) if 'Kim' in s else(False, s), txt)
#lambda_prac = map(functions, iterables(list & strings))