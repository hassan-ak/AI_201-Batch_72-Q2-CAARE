def my_wrapper(func):
    def wrapped():
        print("Before calling the function...")
        func()
        print("After calling the function...")
    return wrapped

@my_wrapper
def say_hello():
    print("Hello, world!")

def main():
    say_hello()

if __name__ == "__main__":
    main()
