import csv

data = [
    ['이름', '점수'],
    ['김철수', 85],
    ['이영희', 92],
    ['박민수', 78],
    ['최수진', 95]
]

with open('grades.csv', 'w', encoding='utf-8', newline='') as f:
    csv.writer(f).writerows(data)
print("학생 성적이 grades.csv에 저장되었습니다.")

print("\n성적 분석 결과:")
scores = []

with open('grades.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)
    
    for name, score in reader:
        print(f"{name}: {score}점")
        scores.append(int(score))

if scores:
    print(f"전체 평균: {sum(scores) / len(scores)}점")