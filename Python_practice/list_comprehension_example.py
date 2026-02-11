num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 짝수 추출
num2 = [number for number in num if number % 2 == 0]
# 제곱
num3 = [number ** 2 for number in num if number % 2 == 0]

print(f"원본 리스트: {num}")
print(f"짝수들: {num2}")
print(f"짝수의 제곱: {num3}")