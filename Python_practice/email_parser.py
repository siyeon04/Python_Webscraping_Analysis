email = str(input("이메일 주소를 입력하세요: "))

user, domain = email.split('@')

print(f"\n사용자명: {user}")
print(f"\n도메인: {domain}")