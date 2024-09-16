money = int(input())
stock = list(map(int, input().split()))

def june():
  left_money = money
  stock_cnt = 0
  
  for i in stock:
    if money > i:
      stock_cnt += left_money // i
      left_money = left_money % i
  return left_money, stock_cnt

def sung():
  left_money = money
  stock_cnt = 0

  for i in range(len(stock) - 4):
    if (stock[i] < stock[i+1] < stock[i+2] < stock[i+3]):
      left_money += stock_cnt * stock[i+3]
    
    if (stock[i] > stock[i+1] > stock[i+2] > stock[i+3]):
      stock_cnt += left_money // stock[i+3]
      left_money = left_money % stock[i+3]
        
  return left_money, stock_cnt

june_money, june_stock = june()
june_m = june_money + (june_stock * stock[-1])

sung_money, sung_stock = sung()
sung_m = sung_money + (sung_stock * stock[-1])

if (june_m > sung_m):
  print("BNP")
elif (june_m == sung_m):
  print("SAMESAME")
else:
  print("TIMING")