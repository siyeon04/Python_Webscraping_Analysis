def fact_rec(n):
    if n <= 1:
        return 1
    return n * fact_rec(n - 1)

def fact_iter(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

nums = [5, 7]
for n in nums:
    print(f"{n}! (재귀) = {fact_rec(n)}")
    print(f"{n}! (반복) = {fact_iter(n)}")