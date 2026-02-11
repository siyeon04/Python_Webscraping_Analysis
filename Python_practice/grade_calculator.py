grade = int(input("점수를 입력하세요: "))

if grade >= 90:
    print(f"\n점수 {grade}점의 학점은 A입니다.")
elif 90 > grade >= 80:
    print(f"\n점수 {grade}점의 학점은 B입니다.")
elif 80 > grade >= 70:
    print(f"\n점수 {grade}점의 학점은 B입니다.")
elif 70 > grade >= 60:
    print(f"\n점수 {grade}점의 학점은 B입니다.")
else:
    print(f"\n점수 {grade}점의 학점은 F입니다.")
