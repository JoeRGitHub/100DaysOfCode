def add(*args):
    print(args[0])
    return sum(args)

print(f"test using *args: {add(5,3,5)}")



def word(n,**kwargs):
    # print(kwargs)
    # print(kwargs["a"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print("test using **kwargs:",n)

word(2,add=3, multiply=5)
