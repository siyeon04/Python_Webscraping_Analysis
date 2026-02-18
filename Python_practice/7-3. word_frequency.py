sample_text = "파이썬 프로그래밍 언어 파이썬 배우기 쉬운 언어 강력한 파이썬 프로그래밍"
with open("words.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

word_count = {}

with open("words.txt", "r", encoding="utf-8") as f:
    words = f.read().split()
    
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

print("단어 빈도 분석 결과:")
for word, count in sorted(word_count.items(), key=lambda x: x[1], reverse=True):
    print(f"{word}: {count}번")