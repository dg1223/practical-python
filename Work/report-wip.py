# report.py
#
# Exercise 2.4

def read_portfolio(filename):
    with open(filename, 'rt') as f:
        portfolio = []
        counter = 0

        for line in f:
            if counter == 0:
                counter += 1 # skip header
                continue

            row = line.split(',')
            portfolio.append((row[0], int(row[1]), float(row[2])))

    return portfolio

def read_portfolio_dict(filename):
    with open(filename, 'rt') as f:
        portfolio = []
        header = f.readline().replace('\n', '')
        counter = 0

        for line in f:
            row = line.split(',')
            record = [row[0], int(row[1]), float(row[2])]

            share_dict = dict(zip(header.split(','), record))
            portfolio.append(share_dict)

    return portfolio

def prices(filename):
    with open(filename, 'rt') as f:
        share_dict = {}
        counter = 0

        for line in f:
            row = line.split(',')

            try:
                share_dict[row[0]] = float(row[1])
            except IndexError:
                pass

    return share_dict

if __name__ == "__main__":
    # print(read_portfolio('Data/portfolio.csv'))
    print(read_portfolio_dict('Data/portfolio.csv'))
    # print(prices('Data/prices.csv'))