# pcost.py
#
# Exercise 1.27
with open('Data/portfolio.csv', 'rt') as f:
    total = 0
    counter = 0

    for line in f:
        if counter == 0:
            counter += 1
            continue

        row = line.split(',')
        total += float(row[2]) * int(row[1])

    print(f"Total cost: {total:.2f}")