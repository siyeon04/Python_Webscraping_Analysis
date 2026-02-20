# main_program.py
import math_operations as mo

#원의 넓이 (반지름 5)
print(f"원의 넓이: {mo.circle_area(5):.2f}")

#직사각형 넓이 (가로 5, 세로 10)
print(f"직사각형 넓이: {mo.rectangle_area(5, 10)}")

#팩토리얼 (5!)
print(f"팩토리얼 5! = {mo.factorial(5)}")

# 4. 최대공약수 (48, 18)
print(f"최대공약수(48, 18) = {mo.gcd(48, 18)}")