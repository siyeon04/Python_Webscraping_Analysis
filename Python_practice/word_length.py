word_list = ['cat', 'elephant', 'dog', 'butterfly', 'ant']

sort_word_list = sorted(word_list, key=len)
long_word = len(sort_word_list[-1])
short_word = len(sort_word_list[0])

print(f'단어 목록: {word_list}')
print(f'\n가장 긴 단어: {sort_word_list[-1]} ({long_word}글자)')
print(f'\n가장 짧은 단어: {sort_word_list[0]} ({short_word}글자)')