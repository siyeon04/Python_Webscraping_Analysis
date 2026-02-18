num1 = [2, 4, 6, 8, 10]
num2 = [1, 3, 5, 7, 12]

def check_nums(nums, label):
    print(f"{label}: {nums}")
   
    even_num = all(num % 2 == 0 for num in nums)
    print(f"모든 수가 짝수인가? {even_num}")
    
    over_ten = any(num > 10 for num in nums)
    print(f"하나라도 10보다 큰 수가 있는가? {over_ten}\n")

check_nums(num1, "숫자 리스트")
check_nums(num2, "숫자 리스트2")