def greet(name, greeting="안녕하세요", suffix="!"):
    return f"{greeting}, {name}님{suffix}"

print(greet("김철수"))

print(f"Hello, John!")

print(greet("이영희", "안녕하세요", "님! 좋은 하루 되세요!"))