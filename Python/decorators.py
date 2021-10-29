def announce(f):
    def wrapper():
        print("Abount to run th function...")
        f()
        print("Done with the function")
    return wrapper

@announce 
def hello():
    print("Hello, wolrd!")

hello()