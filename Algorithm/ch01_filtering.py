grades=[35,70,45,90,65,20,85,75]
print(grades)
#50 'den büyükler geçer

passed=[]
print(passed)

for grade in grades:
    if grade>=50:
        passed.append(grade)
print(passed)