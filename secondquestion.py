def coke_machine():
    total_price = 0
    price = 50
    print('Insert coins(5,10 or 25 cents). Total price is 50 cents.')
    while total_price < price :
        coin = int(input("Insert coin:"))
        if coin in [ 5, 10, 25]:
            total_price += coin
            print(f"total price inserted:{total_price} ")
        else:
            print("invalid coin")    
        change = price - total_price
        if change > 0 :
            print(f"your change is {change} cents")    
        else:
            print("No change is owned")