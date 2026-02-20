import json

user_data = {
    "이름": "김철수",
    "나이": 25,
    "직업": "개발자",
    "취미": ["독서", "영화감상", "코딩"],
    "주소": "서울시 강남구"
}

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(user_data, f, ensure_ascii=False)

print("데이터가 data.json에 저장되었습니다.")

print("\nJSON에서 읽어온 데이터:")
with open('data.json', 'r', encoding='utf-8') as f:
    loaded_data = json.load(f)

for key, value in loaded_data.items():
    print(f"{key}: {value}")