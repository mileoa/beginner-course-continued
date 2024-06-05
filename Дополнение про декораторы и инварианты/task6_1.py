def disable(func):
    def wrapper():
        pass
    return wrapper

def use_itself(func):
    def wrapper(*args):
        return func(func(*args))
    return wrapper

@disable
def delete_db():
    print("Всё подчистили.")

@use_itself
def inc(a):
    return a + 1

delete_db()
print(inc(1))