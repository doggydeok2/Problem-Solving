JH_money = SM_money = int(input())
JH_stock = SM_stock = 0
stock_prices = list(map(int, input().split()))
check = 0
for idx, price in enumerate(stock_prices):
    if JH_money >= price:
        quantity = JH_money // price
        JH_money -= price * quantity
        JH_stock += quantity
    if idx:
        if price - stock_prices[idx - 1] > 0:
            check = 1 if check <= 0 else check + 1
            if check >= 3:
                SM_money += SM_stock * price
                SM_stock = 0
        elif price == stock_prices[idx - 1]:
            check = 0
        else:
            check = -1 if check >= 0 else check - 1
            if check <= -3:
                quantity = SM_money // price
                SM_money -= price * quantity
                SM_stock += quantity
JH_money += JH_stock * stock_prices[-1]
SM_money += SM_stock * stock_prices[-1]
print('BNP' if JH_money > SM_money else 'SAMESAME' if JH_money == SM_money else 'TIMING')
