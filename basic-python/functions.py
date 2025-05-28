def greet():  # def for define: functions
    print("Hello World")
    print("Welcome aboard")


greet()


def greet(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


greet("Gabi", "Minigilda")


def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("Gabi")
print(message)


def increment(number, by):
    return number + by


result = increment(number=2, by=1)
print(result)


def multiply(*numbers):
    print(numbers)


multiply(2, 3, 4, 5)
