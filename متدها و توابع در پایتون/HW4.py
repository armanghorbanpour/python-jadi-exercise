#مجموع مربعات

def sum_of_squares(n1 , n2):
    n1=n1**2
    n2=n2**2
    return n1+n2

number_1=int(input())
number_2=int(input())
print(sum_of_squares(number_1 , number_2))