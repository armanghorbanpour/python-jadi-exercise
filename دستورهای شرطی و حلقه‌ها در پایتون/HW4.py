#طلسم اعداد جادویی

my_input=int(input())

result="معمولی"


if my_input%3==0 and my_input%5==0:
    result= "افسانه ای"
    print(result)
elif my_input%3==0:
    result="جادویی"
    print(result)
elif my_input%5==0:
    result="نفرین شده"
    print(result)
else:
    print(result)