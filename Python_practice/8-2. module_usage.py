import datetime
import random

now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

days = ["월요일", "화요일", "수요일", "목요일", "금요일", "토요일", "일요일"]
day_name = days[now.weekday()]
print(f"포맷된 날짜: {now.strftime('%Y년 %m월 %d일')} {day_name}")

# 임의의 정수 (1~10 사이)
print(f"임의의 숫자: {random.randint(1, 10)}")

# 임의의 실수 (0.0~5.0 사이)
print(f"임의의 실수: {random.uniform(0, 5):.2f}")

# 리스트에서 무작위 선택
fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
print(f"임의의 리스트 요소: {random.choice(fruits)}")

# 리스트 순서 섞기
random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")