shopping_cart = {
    '사과' : {'price': 1000, 'count': 2},
    '바나나' : {'price': 800, 'count': 3},
    '오렌지' : {'price': 1500, 'count': 1}
}

total_price = 0

print("쇼핑 카트:")

for item, info in shopping_cart.items():
    subtotal = info['price'] * info['count']
    print(f'\n{item}: {info["count"]}개 (개당 {info["price"]}원 = {subtotal}원)')

    total_price += subtotal

print(f'\n총 가격: {total_price}원')