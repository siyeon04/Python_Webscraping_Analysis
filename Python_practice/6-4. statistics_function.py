import math

def calculate_statistics(numbers):
    avg = sum(numbers) / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    
    variance = sum((x - avg) ** 2 for x in numbers) / (len(numbers)-1)
    std_dev = math.sqrt(variance)
    
    return avg, max_val, min_val, std_dev

nums = [10, 20, 30, 40, 50]
avg, mx, mn, sd = calculate_statistics(nums)

print(f"숫자들: {nums}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {mx}")
print(f"최솟값: {mn}")
print(f"표준편차: {sd:.2f}")