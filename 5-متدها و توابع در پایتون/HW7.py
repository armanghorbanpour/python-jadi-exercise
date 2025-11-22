#تمرین ورودی از args

def sum_numbers(*args):
    temp=0
    for i in args:
        temp+=i
    return temp

inp=[]
j="0"
while j.isdigit():
    inp.append(int(j))
    j=input()

print(sum_numbers(*inp))