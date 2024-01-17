import urllib.request

import numpy as np
import pandas as pd


def calculate_temp_array(j: int, price_array: np.array, date_array: np.array, temp_array: np.array) -> None:
    for i in range(j, len(price_array)):
        first_price = price_array[i]
        second_price = price_array[i - j]
        # Here we divide by 86400000000000 because the result is in nanoseconds.
        date_result = int((date_array[i] - date_array[i - 1]) / 86400000000000)
        temp_array[i] = ((first_price - second_price) / first_price * 100 / date_result)


def print_one_day_changes(price_array: np.array, date_array: np.array, temp_array: np.array) -> None:
    calculate_temp_array(1, price_array, date_array, temp_array)
    print("The largest percentage decline of the S&P Dow jones index in one day:", temp_array.min())
    print("The highest percentage rise of the S&P Dow jones index in one day:", temp_array.max())
    print("The average rate of change of the S&p Dow Jones index in one day:", temp_array.mean())
    print()


def print_year_changes(price_array: np.array, date_array: np.array, temp_array: np.array) -> None:
    calculate_temp_array(365, price_array, date_array, temp_array)
    print("The largest percentage decline of the S&P Dow jones index in year:", temp_array.min())
    print("The highest percentage rise of the S&P Dow jones index in year:", temp_array.max())
    print("The average rate of change of the S&p Dow Jones index in year:", temp_array.mean())
    print()


def print_moving_average_indicators(price_array: np.array) -> tuple:
    last_five_day = sum(price_array[-5:])
    last_ten_day = sum(price_array[-10:])
    last_fifth_day = sum(price_array[-50:])
    last_two_hundred_day = sum(price_array[-200:])

    print("Average price of the S&P Dow Jones index for the last 5 days: ", last_five_day / 5)
    print("Average price of the S&P Dow Jones index for the last 10 days: ", last_ten_day / 10)
    print("Average price of the S&P Dow Jones index for the last 50 days: ", last_fifth_day / 50)
    print("Average price of the S&P Dow Jones index for the last 200 days: ", last_two_hundred_day / 200)
    print()

    return (last_five_day / 5), (last_fifth_day / 50)


def main():
    file_location = "Performance.xls"
    link = ("https://www.spglobal.com/spdji/en/idsexport/file.xls?redesignExport=true&selectedModule"
            "=PerformanceGraphView&selectedSubModule=Graph&yearFlag=tenYearFlag&indexId=340")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/58.0.3029.110 Safari/537.3'
    }
    req = urllib.request.Request(link, headers=headers)

    response = urllib.request.urlopen(req)

    with open(file_location, 'wb') as file:
        file.write(response.read())

    df = pd.read_excel(file_location, skiprows=range(8), names=["date", "price"])
    date_array = df["date"].to_numpy()
    price_array = df["price"].to_numpy()
    temp_array = np.zeros(len(price_array))

    print("The current price of the S&P Dow Jones index:", price_array[-1])
    print()

    print_one_day_changes(price_array, date_array, temp_array)
    print_year_changes(price_array, date_array, temp_array)
    avg_five, avg_fifth = print_moving_average_indicators(price_array)
    if avg_five > avg_fifth:
        print("S&P Jow Dones Index gives a buy signal")
    else:
        print("S&P Jow Dones Index gives a sell signal")


if __name__ == "__main__":
    main()
