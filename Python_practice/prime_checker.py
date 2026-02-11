num = int(input("숫자를 입력하세요: "))

prime = True
if num < 2:
    prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

if prime:
    print(f"{num}은 소수입니다.")
else:
    print(f"{num}은 소수가 아닙니다.")