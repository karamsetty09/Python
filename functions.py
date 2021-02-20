def great(first_name, last_name):
    print(f"Hi {first_name} {last_name}")
    print("Welcome onboard")


great("sandeep","Karamsetty")
great("Mosh", "Ahmadhani")

def get_greeting(name):
    return f"Hi {name}"

print(great("Hurray","sandeep"))  # Any non-returning function will always returns a none.

message = get_greeting("sandeep")
print(message);


def increment(number, by=1):
    return number + by


print(increment(2, 5))


def multiply(*numbers):  # stores multiple numbers or tuples
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))


def save_user(**user):   # storing a key value pairs 
    print(user)
    print(user["name"])  #how dictionaries work

save_user(id=1, name="sandeep", age=27)


def fizz_buzz(input):
    if (input % 5 == 0) and (input % 3 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input
    

print(fizz_buzz(15))