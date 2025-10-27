print("Passing parameters through decorators:")
print()
def decorator_with_param(param):
    def decorator(func):
        def wrapper(name):
            print(f"{param} {name}!")
        return wrapper
    return decorator

@decorator_with_param("Hello")
def say_name(name):
    return name

say_name('Prajwala')

""" 
step-by-step breakdown:

1. decorator_with_param("Hello") -> returns decorator
2. decorator(say_name) -> returns wrapper
3. say_name is replaced with wrapper
4. say_name('Prajwala') -> calls wrapper('Prajwala')
5. wrapper prints "Hello Prajwala!"

In simpler terms:

- decorator_with_param gets the parameter "Hello".
- decorator gets the function say_name.
- wrapper gets the argument 'Prajwala' and prints the result.

The output is:

Hello Prajwala!

"""
print("---------------------------------------------------------------------------------------")

print("Order of Execution when multiple decorators present:")
print()
def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper

@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()

""" 
The order of execution is:

1. decorator2 wraps say_hello
2. decorator1 wraps the result of decorator2
3. say_hello() is called, which executes decorator1, then decorator2, and finally the original 
say_hello function.

-> In the execution flow why decorator2 is called?

@decorator1
@decorator2
def say_hello():
    print("Hello!")

It's equivalent to:

say_hello = decorator1(decorator2(say_hello))

So first decorator2 is called whose result is wrapped by decorator1

-> Why func() line present in decorators

When you use multiple decorators, each decorator's wrapper function can call the next decorator's 
wrapper function (or the original function) using func().

If you don't include func() in a decorator's wrapper function, it will stop the chain of decorators, 
and any decorators applied after it won't be executed.


"""