fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"과일 목록: {fruits}")
fruit = str(input("찾을 과일을 입력하세요: "))

if fruit in fruits:
    print(f"\n{fruit}가 목록에 있습니다!")
else:
    print(f"\n{fruit}가 목록에 없습니다!")