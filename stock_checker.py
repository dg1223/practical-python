from stock import Stock

a = Stock('GOOG',100,490.10)
b = Stock('AAPL', 50, 122.34)
c = Stock('IBM', 75, 91.75)

print(f"{a.name}, {a.shares}, {a.price} || {a.cost()} || {a.sell(25)}, shares_left = {a.shares} || curr_cost = {a.cost()}")
print(f"{b.name}, {b.shares}, {b.price} || {b.cost()} || {b.sell(25)}, shares_left = {b.shares} || curr_cost = {b.cost()}")
print(f"{c.name}, {c.shares}, {c.price} || {c.cost()} || {c.sell(25)}, shares_left = {c.shares} || curr_cost = {c.cost()}")