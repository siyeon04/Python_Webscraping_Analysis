logs = [
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다\n",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패\n",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음\n",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족\n",
    "2025-07-20 12:15:00 - INFO - 서버가 정상 가동 중입니다\n"
]

with open("app.log", "w", encoding="utf-8") as f:
    f.writelines(logs)

print("로그 파일이 생성되었습니다.")

def filter_logs(level):
    print(f"\n{level} 레벨 로그들:")
    with open("app.log", "r", encoding="utf-8") as f:
        for line in f:
            if f"- {level} -" in line:
                print(line.strip())

filter_logs("ERROR")
filter_logs("WARNING")