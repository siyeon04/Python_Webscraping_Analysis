students = ['김철수', '이영희', '박민수', '최수진']
grades = [85, 92, 78, 95]

print("학생과 점수 매칭: ")
for name, grade in zip(students, grades):
    print(f"{name} : {grade}점")

students_dict = dict(zip(students, grades))

print(f"\n점수별 학생 딕셔너리: {students_dict}")
