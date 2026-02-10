list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

merged_list = list(set(list1) | set(list2))
common_list = list(set(list1) & set(list2))

print(f'\n리스트1: {list1}')
print(f'\n리스트1: {list2}')
print(f'\n병합된 리스트: {merged_list}')
print(f'\n공통 요소: {common_list}')