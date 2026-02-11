multiple_3 = [i for i in range(1, 101) if i % 3 == 0]

total = sum(multiple_3)
count = len(multiple_3)

print(f"1부터 100까지 3의 배수: {multiple_3}")
print(f"\n3의 배수의 합: {total}")
print(f"\n3의 배수의 개수: {count}개")