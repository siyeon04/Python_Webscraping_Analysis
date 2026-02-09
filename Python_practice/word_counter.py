# import re

# a = str(input("문장을 입력하세요: "))

# print(f'공백 제거: {a.replace("  ", " ")}')
# result = re.findall(r'\w+', a)
# word_count = len(result)

# print(f"단어 개수: {word_count}")


# 다른 방법
sentence = input("문장을 입력하세요: ")

words = sentence.split()
clear_sentence = " ".join(words)

print(f"공백 제거: {clear_sentence}")
print(f"단어 개수: {len(words)}개")