import time

def run_time(f):
    def wrapper(n):
        start=time.time()
        result=f(n)
        print(f"{time.time() - start:6.6f}")
        return result
    return wrapper
@run_time
def create_list(n):
    my_list=[]
    for i in range(1,n+1):
        my_list.append(i)
    return my_list
try:
    input_list_lenght=int(input())
except ValueError:
    print("you should enter only integer")
except Exception as e:
    print(f"had error {e}")


#if you wanna see the list, uncomment line 25 and then delete line 26
# print(create_list(input_list_lenght))
create_list(input_list_lenght)