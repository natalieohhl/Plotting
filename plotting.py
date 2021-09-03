import matplotlib.pyplot as plt


def main():
    # 1. load the data (dates, prices) from the csv file into a list of lists

    dates = []
    prices = []
    dates, prices = load_data("stock_data/TSLA.csv")
    print(dates)
    print(prices)

    # 2. plot the graph
    plot_graph(dates, prices, "Tesla")

    pass


def load_data(filename):
    dates = []
    prices = []

    with open(filename) as in_file:
        in_file.readline()
        lines = in_file.readlines()
        for line in lines:
            data = line.split(',')
            # print(data)
            current_date = data[0]  # first item
            current_price = data[4]     # fifth item

            dates.append((current_date))
            prices.append(float(current_price))
            print ("{} - {}".format(current_date, current_price))

    # do the processing
    return dates, prices


def plot_graph(dates, prices, stock_name):
    plt.plot(dates, prices)
    plt.title(stock_name)
    plt.xlabel(stock_name)
    plt.show()
    pass



main()

