#покупка
shares_bought = 2000
price_shares = 40.00
price_shares_bought = price_shares * shares_bought
buy_commission = price_shares_bought * 0.03
print(f"Потратил денег на покупку акций: {price_shares_bought}\n"
      f"Коммиссия при покупке акций: {buy_commission}")

#продажа
sales_share = 2000
price_shares = 42.75
sale_price = sales_share * price_shares
sale_commission = sale_price * 0.03
print(f"Сумма продажи акций: {sale_price}\n"
      f"Коммиссия при продаже: {sale_commission}")

final_result = sale_price - buy_commission - sale_commission
print(f"Оставшаяся сумма денег с вычетом коммиссий: {final_result}")

