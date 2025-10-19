#تمرین فروشگاه مشروط 
price=int(input())
if price < 20_000 :
    print(price)
elif 20_000 <=price < 50_000:
    print(int(price*0.90))
elif price >= 50_000 :
    print(int(price*0.80))