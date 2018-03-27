import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from matplotlib.backends.backend_pdf import PdfPages


#**********************************************get_data****************************************************************#
def get_data(start_time, end_time, data_type, data_stocks, stock_cds):

    list0 = []
    for stock_cd in stock_cds:

        data_stock = data_stocks.loc[data_stocks["Stkcd"] == stock_cd].set_index("Trdmnt")
        list0.append(data_stock.loc[start_time: end_time, [data_type]].fillna(method="pad"))#.fillna(method='pad')


    return list0


#******************************************************get_weight******************************************************#
def get_weight(time, data_stocks, stock_cds):

    market_values = []

    for stock_cd in stock_cds:
        data_stock = data_stocks.loc[data_stocks["Stkcd"] == stock_cd].set_index("Trdmnt")
        market_values.append(float((data_stock.loc[time, ["Msmvttl"]]).tolist()[0]))

    weights = []
    total_market_values = sum(market_values)

    for market_value in market_values:
        weights.append(market_value / total_market_values)

    return weights


#**********************************************get_index***************************************************************#
#def get_index(start_year, end_year):
#
#    indexes = []
#    for year in range(start_year, end_year + 1):
#        for mth in range(1, 13):
#            if mth < 10:
#                Trdmnt = str(year) + "-" + "0" + str(mth)
#            else:
#                Trdmnt = str(year) + "-" + str(mth)
#            indexes.append(Trdmnt)
#
#    return indexes


#**********************************************calculate_portfolio*****************************************************#
def calculate_portfolio(data_of_target_stocks, weights, indexes, data_type):

    time_series = []

    for index in indexes:
        price = 0

        for i in range(0, len(data_of_target_stocks)):
            price = price + weights[i] * float(data_of_target_stocks[i].loc[index, [data_type]].tolist()[0])

        time_series.append(price)

    if data_type == "Mclsprc":
        market_series = []
        for time_value in time_series:
            market_series.append((time_value / time_series[0]) * 100)

        return market_series

    else:
        return time_series



#****************************************************plot_figure*******************************************************#
#def plot_figure(indexes, market_series):
#
#    figure = plt.figure()
#    plt.plot(0)
#    plt.plot(indexes, market_series)
#    market_figure = figure.add_subplot(111)
#    market_figure.set_xlabel("month")
#    market_figure.set_ylabel("value")
#    market_figure.plot(market_series, linewidth=0.5, color="b")
#    market_figure.set_xticklabels(indexes, rotation=40, fontsize=6)
#    market_figure.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])
#    market_figure.grid(True)
#    plt.show()
#    plt.close()
#    return


#**************************************************calculate_covariance************************************************#
def calculate_covariance(X):

    return np.cov(X)
