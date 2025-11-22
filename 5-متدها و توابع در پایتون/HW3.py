#تمرین مثبت یا منفی

def is_positive(number):
    if number>= 0:
        return True
    else:
        return False


number=int(input())
print(is_positive(number))