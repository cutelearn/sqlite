import csv

import matplotlib.pyplot as plt


def read_csv_data(filename, endcode="utf-8"):
    """提出csv檔案中的數據"""
    date, highs, lows, prices = [], [], [], []
    with open(filename, encoding= endcode) as csvFile:
        reader = csv.reader(csvFile)
        listreader = list(reader)
        csvData = listreader[2:-5]
        for row in csvData:
            try:
                current_month = str(row[0])
                high = float(row[4])
                low = float(row[5])
                price = float(row[6])
            except Exception:
                print("有缺值")
            else:
                date.append(current_month)
                highs.append(high)
                lows.append(low)
                prices.append(price)
    return date, highs, lows, prices


def plot_data(date, highs, lows, prices):
    """繪製折線圖"""
    plt.figure(figsize=(12, 8))
    plt.plot(date, highs, 'r', label='High')
    plt.plot(date, lows, 'b', label='Low')
    plt.plot(date, prices, 'g', label='Price')
    plt.legend(loc='best', fontsize=16)
    plt.title('Taiwan Stake', fontsize=24)
    plt.xlabel('Date', fontsize=16)
    plt.ylabel('Price', fontsize=16)
    plt.tick_params(axis='both', labelsize=16, color='red')
    plt.show()


def main():
    date, highs, lows, prices = read_csv_data('stake/STOCK_DAY_1101_202303.csv')
    plot_data(date, highs, lows, prices)


if __name__ == '__main__':
    main()
