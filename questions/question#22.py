def solution(a, b):
    day = [['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU'],[31,29,31,30,31,30,31,31,30,31,30,31]]
    return day[0][(sum(day[1][0:a-1])+b-1)%7]