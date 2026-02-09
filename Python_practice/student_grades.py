# kim = int(input("김철수: "))
# lee = int(input("이영희: "))
# park = int(input("박민수: "))
# choi = int(input("최수진: "))

# student_grades = {
#     "김철수": kim,
#     "이영희": lee, 
#     "박민수": park,
#     "최수진": choi
# }

# avr = sum(student_grades.values()) / len(student_grades)

# print(f"평균 점수: {avr}점")

# 출력 결과에 몇"점"이 안뜸
student_grades = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

print("학생 성적:")

for name, score in student_grades.items():
    print(f"\n{name}: {score}점")

avr = sum(student_grades.values()) / len(student_grades)
print(f"\n평균 점수: {avr}점")