#جادوی حلقه
input_n=int(input())
input_x=int(input())
if (1 <= input_n <= 20) and (1<= input_x <= 1000):
    x=input_x
    n=input_n
    for i in range (n):
        if x%2==1:
            x=(x*2) - 1
        elif x%2==0:
            x=x/2
    print(int(x))
# else:
#     print("meghdar vorodi na motabar")