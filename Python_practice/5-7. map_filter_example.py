nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"원본 숫자: {nums}")

squared = list(map(lambda x: x**2, nums))
print(f"모든 수의 제곱: {squared}")

filtered = list(filter(lambda x: x > 5, nums))
print(f"5보다 큰 수들: {filtered}")

filtered_squared = list(map(lambda x: x**2, filter(lambda x: x > 5, nums)))
print(f"5보다 큰 수들의 제곱: {filtered_squared}")