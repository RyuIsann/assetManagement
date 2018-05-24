import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from matplotlib.backends.backend_pdf import PdfPages
import math
from time import sleep
import csv
import codecs

#**********************************************get_data****************************************************************#
def get_data(start_time, end_time, data_type, data_stocks, stock_cds):

    list0 = []

    if end_time == "end" or end_time == "2017-12":

        for stock_cd in stock_cds:
            data_stock = data_stocks.loc[data_stocks["Stkcd"] == stock_cd].set_index("Trdmnt")
            list0.append(data_stock.loc[start_time: , [data_type]].fillna(method="pad"))
    else :

        for stock_cd in stock_cds:
            data_stock = data_stocks.loc[data_stocks["Stkcd"] == stock_cd].set_index("Trdmnt")
            list0.append(data_stock.loc[start_time: end_time, [data_type]].fillna(method="pad"))


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
def get_index(start_year, end_year):

    indexes = []
    for year in range(start_year, end_year):
        for mth in range(1, 13):
            if mth < 10:
                Trdmnt = str(year) + "-" + "0" + str(mth)
            else:
                Trdmnt = str(year) + "-" + str(mth)
            indexes.append(Trdmnt)

    return indexes


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
def plot_figure(indexes, market_series):

    figure = plt.figure()
    plt.plot(0)
    plt.plot(indexes, market_series)
    market_figure = figure.add_subplot(111)
    market_figure.set_xlabel("month")
    market_figure.set_ylabel("value")
    market_figure.plot(market_series, linewidth=0.5, color="b")
    market_figure.set_xticklabels(indexes, rotation=40, fontsize=6)
    market_figure.set_yticks([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])
    market_figure.grid(True)
    plt.show()
    return


#**************************************************calculate_covariance************************************************#
def calculate_covariance(X):

    return np.cov(X)


#*******************************************************project********************************************************#

data_stocks = pd.read_csv('/Users/ryu_isann/Desktop/TRD_Mnth.csv', encoding='gb2312', low_memory = False)
data_stocks = data_stocks.values
data_stocks = np.array(data_stocks)
data_stocks = np.delete(data_stocks, 0, 0)
data_stocks = np.delete(data_stocks, 0, 0)
data_stock = data_stocks
i = 0
T = 12
start_date = 6

data_stocks_dic = {}

for data in data_stocks:
    data_stocks_dic["t"+data[0]+"d"+data[1]] = float(data[12])

data_stocks_dic_size = {}
for data in data_stocks:
    data_stocks_dic_size["t"+data[0]+"d"+data[1]] = float(data[9])

print(data_stocks_dic)
data_date = []

for i in range(0, len(data_stocks)):
    a = 0
    time = data_stocks[i][1]
    if time not in data_date:
        data_date.append(time)


data_date.sort()
for i in range(0, start_date):
    del(data_date[0])
stock_series = []

for date in data_date:
    stock_pool_for_this_time = []
    for i in range(0, len(data_stocks)):
        if data_stocks[i][1] == date and (data_stocks[i][-2] =="1" or data_stocks[i][-2] == "4"):
            stock_pool_for_this_time.append(data_stocks[i][0])
    stock_series.append(stock_pool_for_this_time)

portfolio1 = []
portfolio2 = []
portfolio3 = []
portfolio4 = []
portfolio5 = []
portfolio6 = []
portfolio7 = []
portfolio8 = []
portfolio9 = []
portfolio10 = []

portfolio11 = []
portfolio21 = []
portfolio31 = []
portfolio41 = []
portfolio51 = []
portfolio61 = []
portfolio71 = []
portfolio81 = []
portfolio91 = []
portfolio101 = []

portfolio1_by_size = []
portfolio2_by_size = []
portfolio3_by_size = []
portfolio4_by_size = []
portfolio5_by_size = []
portfolio6_by_size = []
portfolio7_by_size = []
portfolio8_by_size = []
portfolio9_by_size = []
portfolio10_by_size = []

portfolio1_by_average = []
portfolio2_by_average = []
portfolio3_by_average = []
portfolio4_by_average = []
portfolio5_by_average = []
portfolio6_by_average = []
portfolio7_by_average = []
portfolio8_by_average = []
portfolio9_by_average = []
portfolio10_by_average = []

portfolio1_return_by_size = []
portfolio2_return_by_size = []
portfolio3_return_by_size = []
portfolio4_return_by_size = []
portfolio5_return_by_size = []
portfolio6_return_by_size = []
portfolio7_return_by_size = []
portfolio8_return_by_size = []
portfolio9_return_by_size = []
portfolio10_return_by_size = []

portfolio1_return_by_average = []
portfolio2_return_by_average = []
portfolio3_return_by_average = []
portfolio4_return_by_average = []
portfolio5_return_by_average = []
portfolio6_return_by_average = []
portfolio7_return_by_average = []
portfolio8_return_by_average = []
portfolio9_return_by_average = []
portfolio10_return_by_average = []
i = 0
times = 1


for t in range(0, len(data_date)):

    if t % T == 0:
        times = times+1

        portfolio11 = []
        portfolio21 = []
        portfolio31 = []
        portfolio41 = []
        portfolio51 = []
        portfolio61 = []
        portfolio71 = []
        portfolio81 = []
        portfolio91 = []
        portfolio101 = []

        portfolio1 = []
        portfolio2 = []
        portfolio3 = []
        portfolio4 = []
        portfolio5 = []
        portfolio6 = []
        portfolio7 = []
        portfolio8 = []
        portfolio9 = []
        portfolio10 = []

        portfolio1_by_size = []
        portfolio2_by_size = []
        portfolio3_by_size = []
        portfolio4_by_size = []
        portfolio5_by_size = []
        portfolio6_by_size = []
        portfolio7_by_size = []
        portfolio8_by_size = []
        portfolio9_by_size = []
        portfolio10_by_size = []

        portfolio1_by_average = []
        portfolio2_by_average = []
        portfolio3_by_average = []
        portfolio4_by_average = []
        portfolio5_by_average = []
        portfolio6_by_average = []
        portfolio7_by_average = []
        portfolio8_by_average = []
        portfolio9_by_average = []
        portfolio10_by_average = []

        size1 = []
        size2 = []
        size3 = []
        size4 = []
        size5 = []
        size6 = []
        size7 = []
        size8 = []
        size9 = []
        size10 = []

        stock_pool = stock_series[t]

        tag1 = []
        tag2 = []
        volumn = []
        i = 0

        for i in range(0, len(stock_series[t])):
            volumn.append(data_stocks_dic_size["t"+stock_series[t][i]+"d"+data_date[t]])
            tag1.append("t"+stock_series[t][i]+"d"+data_date[t])
            tag2.append(stock_series[t][i])

        sorted_stock_pool = tag1
        sorted_stock_pool0 = tag2
        print(volumn)

        for x in range(0, len(stock_series[t])-1):
            for y in range(0, len(stock_series[t])-x-1):
                if volumn[y] > volumn[y+1]:
                    tmp = sorted_stock_pool[y]
                    sorted_stock_pool[y] = sorted_stock_pool[y+1]
                    sorted_stock_pool[y + 1] = tmp
                    tmp = sorted_stock_pool0[y]
                    sorted_stock_pool0[y] = sorted_stock_pool0[y + 1]
                    sorted_stock_pool0[y + 1] = tmp
                    tmp = volumn[y]
                    volumn[y] = volumn[y+1]
                    volumn[y+1] = tmp



        print(volumn)
        print(sorted_stock_pool0)

        divid_point = len(sorted_stock_pool)/10
        i = 0
        for i in range(0, len(sorted_stock_pool)):
            if divid_point >= i+1 :
                portfolio1.append(sorted_stock_pool[i])
                portfolio11.append(sorted_stock_pool0[i])
                size1.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 2 * divid_point >= i+1 and divid_point < i+1:
                portfolio2.append(sorted_stock_pool[i])
                portfolio21.append(sorted_stock_pool0[i])
                size2.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 3 * divid_point >= i+1 and 2 * divid_point < i+1:
                portfolio3.append(sorted_stock_pool[i])
                portfolio31.append(sorted_stock_pool0[i])
                size3.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 4 * divid_point >= i+1 and 3 * divid_point < i+1:
                portfolio4.append(sorted_stock_pool[i])
                portfolio41.append(sorted_stock_pool0[i])
                size4.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 5 * divid_point >= i+1 and 4 * divid_point < i+1:
                portfolio5.append(sorted_stock_pool[i])
                portfolio51.append(sorted_stock_pool0[i])
                size5.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 6 * divid_point >= i+1 and 5 * divid_point < i+1:
                portfolio6.append(sorted_stock_pool[i])
                portfolio61.append(sorted_stock_pool0[i])
                size6.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 7 * divid_point >= i+1 and 6 * divid_point < i+1:
                portfolio7.append(sorted_stock_pool[i])
                portfolio71.append(sorted_stock_pool0[i])
                size7.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 8 * divid_point >= i+1 and 7 * divid_point < i+1:
                portfolio8.append(sorted_stock_pool[i])
                portfolio81.append(sorted_stock_pool0[i])
                size8.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 9 * divid_point >= i+1 and 8 * divid_point < i+1:
                portfolio9.append(sorted_stock_pool[i])
                portfolio91.append(sorted_stock_pool0[i])
                size9.append(data_stocks_dic_size[sorted_stock_pool[i]])
            elif 10 * divid_point >= i+1 and 9 * divid_point < i+1:
                portfolio10.append(sorted_stock_pool[i])
                portfolio101.append(sorted_stock_pool0[i])
                size10.append(data_stocks_dic_size[sorted_stock_pool[i]])
        '''print(portfolio11)
        print(portfolio21)
        print(portfolio31)
        print(portfolio41)
        print(portfolio51)
        print(portfolio61)
        print(portfolio71)
        print(portfolio81)
        print(portfolio91)
        print(portfolio101)'''
        for size in size1:
            portfolio1_by_size.append(size/sum(size1))
            portfolio1_by_average.append(1 / len(size1))
        for size in size2:
            portfolio2_by_size.append(size/sum(size2))
            portfolio2_by_average.append(1 / len(size2))
        for size in size3:
            portfolio3_by_size.append(size/sum(size3))
            portfolio3_by_average.append(1 / len(size3))
        for size in size4:
            portfolio4_by_size.append(size/sum(size4))
            portfolio4_by_average.append(1 / len(size4))
        for size in size5:
            portfolio5_by_size.append(size/sum(size5))
            portfolio5_by_average.append(1 / len(size5))
        for size in size6:
            portfolio6_by_size.append(size/sum(size6))
            portfolio6_by_average.append(1 / len(size6))
        for size in size7:
            portfolio7_by_size.append(size/sum(size7))
            portfolio7_by_average.append(1 / len(size7))
        for size in size8:
            portfolio8_by_size.append(size/sum(size8))
            portfolio8_by_average.append(1 / len(size8))
        for size in size9:
            portfolio9_by_size.append(size/sum(size9))
            portfolio9_by_average.append(1 / len(size9))
        for size in size10:
            portfolio10_by_size.append(size/sum(size10))
            portfolio10_by_average.append(1 / len(size10))

        '''print(portfolio1_by_size)
        print(len(portfolio1_by_size))
        print()
        print(portfolio2_by_size)
        print(len(portfolio2_by_size))
        print()
        print(portfolio3_by_size)
        print(len(portfolio3_by_size))
        print()
        print(portfolio4_by_size)
        print(len(portfolio4_by_size))
        print()
        print(portfolio5_by_size )
        print(len(portfolio5_by_size))
        print()
        print(portfolio6_by_size)
        print(len(portfolio6_by_size))
        print()
        print(portfolio7_by_size )
        print(len(portfolio7_by_size))
        print()
        print(portfolio8_by_size )
        print(len(portfolio8_by_size))
        print()
        print(portfolio9_by_size )
        print(len(portfolio9_by_size))
        print()
        print(portfolio10_by_size )
        print(len(portfolio10_by_size))
        print()
        print(portfolio1_by_average )
        print(len(portfolio1_by_average))
        print()
        print(portfolio2_by_average )
        print(len(portfolio2_by_average))
        print()
        print(portfolio3_by_average)
        print(len(portfolio3_by_average))
        print()
        print(portfolio4_by_average)
        print(len(portfolio4_by_average))
        print()
        print(portfolio5_by_average)
        print(len(portfolio5_by_average))
        print()
        print(portfolio6_by_average )
        print(len(portfolio6_by_average))
        print()
        print(portfolio7_by_average)
        print(len(portfolio7_by_average))
        print()
        print(portfolio8_by_average)
        print(len(portfolio8_by_average))
        print()
        print(portfolio9_by_average)
        print(len(portfolio9_by_average))
        print()
        print(portfolio10_by_average)
        print(len(portfolio10_by_average))
        print()

        print("\n\n\n\n\n\n\n\n\n\n\n")'''




    number = 0
    '''print(sum(portfolio1_by_size))
    print(sum(portfolio2_by_size))
    print(sum(portfolio3_by_size))
    print(sum(portfolio4_by_size))
    print(sum(portfolio5_by_size))
    print(sum(portfolio6_by_size))
    print(sum(portfolio7_by_size))
    print(sum(portfolio8_by_size))
    print(sum(portfolio9_by_size))
    print(sum(portfolio10_by_size))'''
    for number in range(0, len(portfolio11)):
        if "t" + portfolio11[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio11[number] + "d" + data_date[t]]) != True:
                portfolio1_by_size[number] = portfolio1_by_size[number] * ( data_stocks_dic["t" + portfolio11[number] + "d" + data_date[t]] + 1)
                portfolio1_by_average[number] = portfolio1_by_average[number] * ( data_stocks_dic["t" + portfolio11[number] + "d" + data_date[t]] + 1)

        '''else:
            portfolio1_by_size[number] = 0
            portfolio1_by_average[number] = 0'''


    number = 0
    for number in range(0, len(portfolio21)):
        if "t" + portfolio21[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio21[number] + "d" + data_date[t]]) != True:
                portfolio2_by_size[number] = portfolio2_by_size[number] * ( data_stocks_dic["t" + portfolio21[number] + "d" + data_date[t]] + 1)
                portfolio2_by_average[number] = portfolio2_by_average[number] * ( data_stocks_dic["t" + portfolio21[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio2_by_size[number] = 0
            portfolio2_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio31)):
        if "t" + portfolio31[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio31[number] + "d" + data_date[t]]) != True:
                portfolio3_by_size[number] = portfolio3_by_size[number] * ( data_stocks_dic["t" + portfolio31[number] + "d" + data_date[t]] + 1)
                portfolio3_by_average[number] = portfolio3_by_average[number] * ( data_stocks_dic["t" + portfolio31[number] + "d" + data_date[t]] + 1)
                if math.isnan(data_stocks_dic["t" + portfolio31[number] + "d" + data_date[t]]):
                    print("shit happens")

        '''else:
            portfolio3_by_size[number] = 0
            portfolio3_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio41)):
        if "t" + portfolio41[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio41[number] + "d" + data_date[t]] )!= True:
                portfolio4_by_size[number] = portfolio4_by_size[number] * ( data_stocks_dic["t" + portfolio41[number] + "d" + data_date[t]] + 1)
                portfolio4_by_average[number] = portfolio4_by_average[number] * ( data_stocks_dic["t" + portfolio41[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio4_by_size[number] = 0
            portfolio4_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio51)):
        if "t" + portfolio51[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio51[number] + "d" + data_date[t]]) != True:
                portfolio5_by_size[number] = portfolio5_by_size[number] * ( data_stocks_dic["t" + portfolio51[number] + "d" + data_date[t]] + 1)
                portfolio5_by_average[number] =portfolio5_by_average[number] * ( data_stocks_dic["t" + portfolio51[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio5_by_size[number] = 0
            portfolio5_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio61)):
        if "t" + portfolio61[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio61[number] + "d" + data_date[t]]) != True:
                portfolio6_by_size[number] = portfolio6_by_size[number] * ( data_stocks_dic["t" + portfolio61[number] + "d" + data_date[t]] + 1)
                portfolio6_by_average[number] = portfolio6_by_average[number] * ( data_stocks_dic["t" + portfolio61[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio6_by_size[number] = 0
            portfolio6_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio71)):
        if "t" + portfolio71[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio71[number] + "d" + data_date[t]]) != True:
                portfolio7_by_size[number] = portfolio7_by_size[number] * ( data_stocks_dic["t" + portfolio71[number] + "d" + data_date[t]] + 1)
                portfolio7_by_average[number] = portfolio7_by_average[number] * ( data_stocks_dic["t" + portfolio71[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio7_by_size[number] = 0
            portfolio7_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio81)):
        if "t" + portfolio81[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio81[number] + "d" + data_date[t]] )!= True:
                portfolio8_by_size[number] = portfolio8_by_size[number] * ( data_stocks_dic["t" + portfolio81[number] + "d" + data_date[t]] + 1)
                portfolio8_by_average[number] = portfolio8_by_average[number] * ( data_stocks_dic["t" + portfolio81[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio8_by_size[number] = 0
            portfolio8_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio91)):
        if "t" + portfolio91[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio91[number] + "d" + data_date[t]] )!= True:
                portfolio9_by_size[number] = portfolio9_by_size[number] * ( data_stocks_dic["t" + portfolio91[number] + "d" + data_date[t]] + 1)
                portfolio9_by_average[number] = portfolio9_by_average[number] * ( data_stocks_dic["t" + portfolio91[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio9_by_size[number] = 0
            portfolio9_by_average[number] = 0'''

    number = 0
    for number in range(0, len(portfolio101)):
        if "t" + portfolio101[number] + "d" + data_date[t] in data_stocks_dic.keys():
            if math.isnan(data_stocks_dic["t" + portfolio101[number] + "d" + data_date[t]] )!= True:
                portfolio10_by_size[number] = portfolio10_by_size[number] * ( data_stocks_dic["t" + portfolio101[number] + "d" + data_date[t]] + 1)
                portfolio10_by_average[number] = portfolio10_by_average[number] * ( data_stocks_dic["t" + portfolio101[number] + "d" + data_date[t]] + 1)
        '''else:
            portfolio10_by_size[number] = 0
            portfolio10_by_average[number] = 0'''

    if t%T == (T-1):
        portfolio1_return_by_average.append((sum(portfolio1_by_average)-1)/12)
        portfolio2_return_by_average.append((sum(portfolio2_by_average)-1)/12)
        portfolio3_return_by_average.append((sum(portfolio3_by_average)-1)/12)
        portfolio4_return_by_average.append((sum(portfolio4_by_average)-1)/12)
        portfolio5_return_by_average.append((sum(portfolio5_by_average)-1)/12)
        portfolio6_return_by_average.append((sum(portfolio6_by_average)-1)/12)
        portfolio7_return_by_average.append((sum(portfolio7_by_average)-1)/12)
        portfolio8_return_by_average.append((sum(portfolio8_by_average)-1)/12)
        portfolio9_return_by_average.append((sum(portfolio9_by_average)-1)/12)
        portfolio10_return_by_average.append((sum(portfolio10_by_average)-1)/12)
        portfolio1_return_by_size.append((sum(portfolio1_by_size)-1)/12)
        portfolio2_return_by_size.append((sum(portfolio2_by_size)-1)/12)
        portfolio3_return_by_size.append((sum(portfolio3_by_size)-1)/12)
        portfolio4_return_by_size.append((sum(portfolio4_by_size)-1)/12)
        portfolio5_return_by_size.append((sum(portfolio5_by_size)-1)/12)
        portfolio6_return_by_size.append((sum(portfolio6_by_size)-1)/12)
        portfolio7_return_by_size.append((sum(portfolio7_by_size)-1)/12)
        portfolio8_return_by_size.append((sum(portfolio8_by_size)-1)/12)
        portfolio9_return_by_size.append((sum(portfolio9_by_size)-1)/12)
        portfolio10_return_by_size.append((sum(portfolio10_by_size)-1)/12)





print(portfolio1_return_by_size)
print(portfolio2_return_by_size)
print(portfolio3_return_by_size)
print(portfolio4_return_by_size)
print(portfolio5_return_by_size)
print(portfolio6_return_by_size)
print(portfolio7_return_by_size)
print(portfolio8_return_by_size)
print(portfolio9_return_by_size)
print(portfolio10_return_by_size)

print("\n\n\n\n\n\n\n")

print(portfolio1_return_by_average)
print(portfolio2_return_by_average)
print(portfolio3_return_by_average)
print(portfolio4_return_by_average)
print(portfolio5_return_by_average)
print(portfolio6_return_by_average)
print(portfolio7_return_by_average)
print(portfolio8_return_by_average)
print(portfolio9_return_by_average)
print(portfolio10_return_by_average)


'''a = len(portfolio1_return_by_size)
b = len(portfolio2_return_by_size)
c = len(portfolio3_return_by_size)
d = len(portfolio4_return_by_size)
e = len(portfolio5_return_by_size)
f = len(portfolio6_return_by_size)
g = len(portfolio7_return_by_size)
h = len(portfolio8_return_by_size)
i = len(portfolio9_return_by_size)
j = len(portfolio10_return_by_size)

a0 = len(portfolio1_return_by_average)
b0 = len(portfolio2_return_by_average)
c0 = len(portfolio3_return_by_average)
d0 = len(portfolio4_return_by_average)
e0 = len(portfolio5_return_by_average)
f0 = len(portfolio6_return_by_average)
g0 = len(portfolio7_return_by_average)
h0 = len(portfolio8_return_by_average)
i0 = len(portfolio9_return_by_average)
j0 = len(portfolio10_return_by_average)


print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)
print(j)



print(a0)
print(b0)
print(c0)
print(d0)
print(e0)
print(f0)
print(g0)
print(h0)
print(i0)
print(j0)

value1 = 1
value2 = 1
value3 = 1
value4 = 1
value5 = 1
value6 = 1
value7 = 1
value8 = 1
value9 = 1
value10 = 1
value01 = [1]
value02 = [1]
value03 = [1]
value04 = [1]
value05 = [1]
value06 = [1]
value07 = [1]
value08 = [1]
value09 = [1]
value010 = [1]'''

'''for i in range(0, len(portfolio1_return_by_size)):
    value1 = value1 * (1 + portfolio1_return_by_size[i])
    value01.append( value1)
    value2 = value2 * (1 + portfolio2_return_by_size[i])
    value02.append( value2)
    value3 = value3 * (1 + portfolio3_return_by_size[i])
    value03.append(value3)
    value4 = value4 * (1 + portfolio4_return_by_size[i])
    value04.append(value4)
    value5 = value5 * (1 + portfolio5_return_by_size[i])
    value05.append(value5)
    value6 = value6 * (1 + portfolio6_return_by_size[i])
    value06.append(value6)
    value7 = value7 * (1 + portfolio7_return_by_size[i])
    value07.append(value7)
    value8 = value8 * (1 + portfolio8_return_by_size[i])
    value08.append( value8)
    value9 = value9 * (1 + portfolio9_return_by_size[i])
    value09.append( value9)
    value10 = value10 * (1 + portfolio10_return_by_size[i])
    value010.append(value10)

print(value01[-1]/len(value01))
print(value02[-1]/len(value02))
print(value03[-1]/len(value03))
print(value04[-1]/len(value04))
print(value05[-1]/len(value05))
print(value06[-1]/len(value06))
print(value07[-1]/len(value07))
print(value08[-1]/len(value08))
print(value09[-1]/len(value09))
print(value010[-1]/len(value010))'''



'''return_series_average = []
return_series_size = []
for i in range(0, len(portfolio10_return_by_averaget)):
    return_series_average.append(portfolio10_return_by_average[i] - portfolio1_return_by_average[i])
    return_series_size.append(portfolio10_return_by_size[i] - portfolio1_return_by_size[i])
'''
'''print(return_series_average)
print(return_series_size)
plt.plot(return_series_average, label="Average")
plt.plot(return_series_size, label="Size")'''
'''
print(sum(portfolio1_return_by_size)/len(value01))
print(sum(portfolio2_return_by_size)/len(value02))
print(sum(portfolio3_return_by_size)/len(value03))
print(sum(portfolio4_return_by_size)/len(value04))
print(sum(portfolio5_return_by_size)/len(value05))
print(sum(portfolio6_return_by_size)/len(value06))
print(sum(portfolio7_return_by_size)/len(value07))
print(sum(portfolio8_return_by_size)/len(value08))
print(sum(portfolio9_return_by_size)/len(value09))
print(sum(portfolio10_return_by_size)/len(value010))'''

'''plt.plot(value01, label="1")
plt.plot(value02, label="2")
plt.plot(value03, label="3")
plt.plot(value04, label="4")
plt.plot(value05, label="5")
plt.plot(value06, label="6")
plt.plot(value07, label="7")
plt.plot(value08, label="8")
plt.plot(value09, label="9")
plt.plot(value010, label="10")
plt.legend()
plt.show()
'''
year = 1991
with codecs.open('/Users/ryu_isann/Desktop/optional_hw.csv', 'w','gbk') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(
        ["","Small", "2", "3", "4", "5", "6", "7", "8", "9", "Big"])

    for i in range(0, len(portfolio10_return_by_average)):
        row = []
        row.append(str(year+0.7)+"-"+str(year+1+0.6))
        year = year + 1
        row.append(  portfolio1_return_by_average[i]  )
        row.append(portfolio2_return_by_average[i])
        row.append(portfolio3_return_by_average[i])
        row.append(portfolio4_return_by_average[i])
        row.append(portfolio5_return_by_average[i])
        row.append(portfolio6_return_by_average[i])
        row.append(portfolio7_return_by_average[i])
        row.append(portfolio8_return_by_average[i])
        row.append(portfolio9_return_by_average[i])
        row.append(portfolio10_return_by_average[i])
        writer.writerow(row)
    writer.writerow(
        ["","Small", "2", "3", "4", "5", "6", "7", "8", "9", "Big"])
    year = 1991
    for i in range(0, len(portfolio10_return_by_average)):
        row = []
        row.append(str(year + 0.7) + "-" + str(year + 1 + 0.6))
        year = year + 1
        row.append(portfolio1_return_by_size[i]  )
        row.append(portfolio2_return_by_size[i])
        row.append(portfolio3_return_by_size[i])
        row.append(portfolio4_return_by_size[i])
        row.append(portfolio5_return_by_size[i])
        row.append(portfolio6_return_by_size[i])
        row.append(portfolio7_return_by_size[i])
        row.append(portfolio8_return_by_size[i])
        row.append(portfolio9_return_by_size[i])
        row.append(portfolio10_return_by_size[i])
        writer.writerow(row)
    csvFile.close()

#for short and long#
strategy_average = []
strategy_size = []
for n in range(0, len(portfolio10_return_by_average)):
    strategy_average.append(portfolio1_return_by_average[n] - portfolio10_return_by_average[n])
    strategy_size.append(portfolio1_return_by_size[n] - portfolio10_return_by_size[n])

with codecs.open('/Users/ryu_isann/Desktop/optional_hw_short_and_long.csv', 'w','gbk') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(
        ["","average", "size"])
    year = 1991

    for i in range(0, len(portfolio10_return_by_average)):
        row = []
        row.append(str(year + 0.7) + "-" + str(year + 1 + 0.6))
        year = year + 1
        row.append(  strategy_average[i]  )
        row.append(strategy_size[i])
        writer.writerow(row)
    csvFile.close()

plt.plot(strategy_average, label="average")
plt.plot(strategy_size, label="size")
plt.legend()
plt.show()

