num1 = int(input("상품 가격을 입력하세요: "))
num2 = int(input("\n할인율을 입력하세요(%): "))
sale = num1 * (num2)/100
print(f"\n원래 가격: {num1}원")
print(f"\n할인율: {num2}%")
print(f"\n할인 금액: {sale:.0f}원")
print(f"\n최종 가격: {num1 - sale:.0f}원")