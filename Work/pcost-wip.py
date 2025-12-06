# pcost.py
#
# Exercise 1.27, 1.30, 'Data/portfolio.csv'

def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        total = 0
        counter = 0

        for line in f:
            if counter == 0:
                counter += 1
                continue

            row = line.split(',')
            total += float(row[2]) * int(row[1])

    return f"Total cost: {total:.2f}"

if __name__ == "__main__":
    print(portfolio_cost('Data/portfolio.csv'))