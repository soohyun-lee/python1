A = {'age': 30, '국어': 83, '영어': 100, '수학': 37}
B = {'age': 42, '국어': 52, '영어': 56, '수학': 47}
C = {'age': 27, '국어': 40, '영어': 97, '수학': 89}
D = {'age': 60, '국어': 90, '영어': 79, '수학': 97}
people = [A, B, C, D]
C_avg = sum([x for x in C.values()])/len(C)
print(C_avg)
age_sum = sum([x['age'] for x in people])
print(age_sum)