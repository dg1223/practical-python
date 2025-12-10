# Decorator is a function that takes another function as input

# pass func() as an object
def decorator(func):
    def wrapper():
        print("before")
        func()
        print("after")

    return wrapper

@decorator
def hello():
    print("Hello!")

hello()