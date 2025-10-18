#دیکشنری حاوی میوه
fruit_prices= {
    "apple": 1500 ,
    "banana": 1000 ,
    "orange": 1200
}
fruit_prices.pop("apple")

#for change value we have two ways:
#first solution:
fruit_prices.update({"banana":1100})

#second solution:
# fruit_prices["banana"]=1100

print(fruit_prices)