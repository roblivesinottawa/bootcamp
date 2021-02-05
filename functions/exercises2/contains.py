def contains_milk(*args):
    if "milk" in args:
        return True
    return False

print(contains_milk("green", False, 45, "hello", "coffee", True, "milk"))