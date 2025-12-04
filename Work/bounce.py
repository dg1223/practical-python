# bounce.py
#
# Exercise 1.5
height = 100
bounce = 1

while height > 0 and bounce <= 10:
    height = round(height * 0.6, 4)
    bounce += 1

    print(f"{bounce-1} {height}")