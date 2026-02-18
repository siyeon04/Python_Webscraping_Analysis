grade = 85
result = "합격" if grade >= 80 else "불합격"
print(f"점수: {grade}, 결과: {result}")

age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

a, b = 42, 36
max_val = a if a > b else b
print(f"숫자들의 최대값: {max_val}")

nums = [5, -7, 12, 8, -2, 23, 10]
positives = [n for n in nums if n > 0]
print(f"양수들: {positives}")