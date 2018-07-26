import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gs
from matplotlib.backends.backend_pdf import PdfPages
import math
from time import sleep
import csv
import codecs



class PortfolioSort:

    def __init__(self, data_stocks, id_index, return_index, size_index, year_index, month_index, T, compare_index, compare_index1=-1, sort_num1=1, sort_num2=1, start_date=0):

        self.data_stocks = data_stocks
        self.compare_index = compare_index
        self.sort_num1 = sort_num1
        self.sort_num2 = sort_num2
        self.start_date = start_date
        self.T = T
        self.year_index = year_index
        self.month_index = month_index
        self.return_index = return_index
        self.id_index = id_index
        self.compare_index1 = compare_index1
        self.size_index = size_index

    def sortByIndex(self):

        data_stocks = self.data_stocks
        data_stocks = data_stocks.values
        data_stocks = np.array(data_stocks)
        monthly_return_size = []
        monthly_return_ave = []

        data_stocks_dic = {}
        for data in data_stocks:
            date_0 = "0" * (6 - len(str(data[self.id_index]))) + str(data[self.id_index])
            year_0 = str(data[self.year_index])
            month_0 = "0" * (2 - len(str(data[self.month_index]))) + str(data[self.month_index])
            data_stocks_dic["t" + date_0 + "d" + year_0 + month_0] = float(data[self.return_index])

        data_stocks_dic_compare = {}
        for data in data_stocks:
            date_0 = "0" * (6 - len(str(data[self.id_index]))) + str(data[self.id_index])
            year_0 = str(data[self.year_index])
            month_0 = "0" * (2 - len(str(data[self.month_index]))) + str(data[self.month_index])
            data_stocks_dic_compare["t" + date_0 + "d" + year_0 + month_0] = float(data[self.compare_index])

        if self.compare_index1 != -1 :
            data_stocks_dic_compare1 = {}
            for data in data_stocks:
                date_0 = "0" * (6 - len(str(data[self.id_index]))) + str(data[self.id_index])
                year_0 = str(data[self.year_index])
                month_0 = "0" * (2 - len(str(data[self.month_index]))) + str(data[self.month_index])
                data_stocks_dic_compare1["t" + date_0 + "d" + year_0 + month_0] = float(data[self.compare_index1])
        else:
            data_stocks_dic_compare1 = data_stocks_dic_compare

        data_stocks_dic_size = {}
        for data in data_stocks:
            date_0 = "0" * (6 - len(str(data[self.id_index]))) + str(data[self.id_index])
            year_0 = str(data[self.year_index])
            month_0 = "0" * (2 - len(str(data[self.month_index]))) + str(data[self.month_index])
            data_stocks_dic_size["t" + date_0 + "d" + year_0 + month_0] = data[self.size_index]

        data_date = []
        for data in data_stocks:
            year_0 = str(data[self.year_index])
            month_0 = "0" * (2 - len(str(data[self.month_index]))) + str(data[self.month_index])
            time = year_0 + month_0
            if time not in data_date:
                data_date.append(time)
        data_date.sort()

        stock_series = []

        for date in data_date:
            stock_pool_for_this_time = []

            for i in range(0, len(data_stocks)):

                year_0 = str(data_stocks[i][self.year_index])
                month_0 = "0" * (2 - len(str(data_stocks[i][self.month_index]))) + str(data_stocks[i][self.month_index])

                if year_0 + month_0 == date:
                    stock_pool_for_this_time.append("0" * (6 - len(str(data_stocks[i][self.id_index]))) + str(data_stocks[i][self.id_index]))
            stock_series.append(stock_pool_for_this_time)

        portfolio0 = []
        for num0 in range(0, self.sort_num1 * self.sort_num2):
            portfolio0.append([])

        portfolio1 = []
        for num1 in range(0, self.sort_num2 * self.sort_num1):
            portfolio1.append([])

        portfolio_by_size = []
        for num2 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_by_size.append([])

        portfolio_by_average = []
        for num3 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_by_average.append([])

        portfolio_by_size1 = []
        for num2 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_by_size1.append([])

        portfolio_by_average1 = []
        for num3 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_by_average1.append([])

        portfolio_return_by_size = []
        for num4 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_return_by_size.append([])

        portfolio_return_by_average = []
        for num5 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_return_by_average.append([])

        portfolio_return_by_average1 = []
        for num3 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_return_by_average1.append([])

        portfolio_return_by_size1 = []
        for num4 in range(0, self.sort_num2 * self.sort_num1):
            portfolio_return_by_size1.append([])

        test = 0
        for t in range(self.start_date, len(data_date)):
            if t % self.T == self.start_date % self.T:

                test = 1

                portfolio0 = []
                for num0 in range(0, self.sort_num1 * self.sort_num2):
                    portfolio0.append([])

                portfolio1 = []
                for num1 in range(0, self.sort_num2 * self.sort_num1):
                    portfolio1.append([])

                portfolio_by_size = []
                for num2 in range(0, self.sort_num2 * self.sort_num1):
                    portfolio_by_size.append([])

                portfolio_by_average = []
                for num3 in range(0, self.sort_num2 * self.sort_num1):
                    portfolio_by_average.append([])

                portfolio_by_size1 = []
                for num2 in range(0, self.sort_num2 * self.sort_num1):
                    portfolio_by_size1.append([])

                portfolio_by_average1 = []
                for num3 in range(0, self.sort_num2 * self.sort_num1):
                    portfolio_by_average1.append([])

                size = []
                for num4 in range(0, self.sort_num1 * self.sort_num2):
                    size.append([])

                compare1 = []
                for num5 in range(0, self.sort_num2 * self.sort_num1):
                    compare1.append([])

                compare2 = []
                for num6 in range(0, self.sort_num1 * self.sort_num2):
                    compare2.append([])

                tag1 = []
                tag2 = []
                volumn_compare2 = []
                volumn_compare1 = []

                for i in range(0, len(stock_series[t])):
                    volumn_compare1.append(float(data_stocks_dic_compare["t" + stock_series[t][i] + "d" + data_date[t]]))
                    volumn_compare2.append(float(data_stocks_dic_compare1["t" + stock_series[t][i] + "d" + data_date[t]]))
                    tag1.append("t" + stock_series[t][i] + "d" + data_date[t])
                    tag2.append(stock_series[t][i])

                sorted_stock_pool = tag1
                sorted_stock_pool0 = tag2

                for x in range(0, len(stock_series[t]) - 1):
                    for y in range(0, len(stock_series[t]) - x - 1):
                        if volumn_compare1[y] > volumn_compare1[y + 1]:
                            tmp = sorted_stock_pool[y]
                            sorted_stock_pool[y] = sorted_stock_pool[y + 1]
                            sorted_stock_pool[y + 1] = tmp
                            tmp = sorted_stock_pool0[y]
                            sorted_stock_pool0[y] = sorted_stock_pool0[y + 1]
                            sorted_stock_pool0[y + 1] = tmp
                            tmp = volumn_compare1[y]
                            volumn_compare1[y] = volumn_compare1[y + 1]
                            volumn_compare1[y + 1] = tmp

                portfolioa = []
                for num7 in range(0, self.sort_num1):
                    portfolioa.append([])

                compare2a = []
                for num8 in range(0, self.sort_num1):
                    compare2a.append([])

                return_ = []
                for num9 in range(0, self.sort_num1):
                    return_.append([])

                divid_point = len(sorted_stock_pool) / self.sort_num1

                for i in range(0, len(sorted_stock_pool)):
                    portfolioa[int(i/divid_point)].append(sorted_stock_pool0[i])
                    compare2a[int(i/divid_point)].append(data_stocks_dic_compare1[sorted_stock_pool[i]])
                    return_[int(i/divid_point)].append(sorted_stock_pool[i])

                for j in range(0, len(portfolioa)):

                    for x in range(0, len(portfolioa[j]) - 1):
                        for y in range(0, len(portfolioa[j]) - x - 1):
                            if compare2a[j][y] > compare2a[j][y + 1]:
                                tmp = portfolioa[j][y]
                                portfolioa[j][y] = portfolioa[j][y + 1]
                                portfolioa[j][y + 1] = tmp
                                tmp = return_[j][y]
                                return_[j][y] = return_[j][y + 1]
                                return_[j][y + 1] = tmp
                                tmp = compare2a[j][y]
                                compare2a[j][y] = compare2a[j][y + 1]
                                compare2a[j][y + 1] = tmp

                    divid_point = len(portfolioa[j]) / self.sort_num2
                    for i in range(0, len(portfolioa[j])):
                        portfolio1[j * self.sort_num2 + int(i/divid_point)].append(portfolioa[j][i])
                        size[j * self.sort_num2 + int(i/divid_point)].append(float(data_stocks_dic_size["t" + portfolioa[j][i] + "d" + data_date[t]]))

                for i in range(0, len(size)):
                    for sizenum in size[i]:
                        portfolio_by_size[i].append(sizenum / sum(size[i]))
                        portfolio_by_average[i].append( 1 / len(size[i]))
                        portfolio_by_size1[i].append(sizenum / sum(size[i]))
                        portfolio_by_average1[i].append(1 / len(size[i]))

            basket_ave = []
            basket_size = []

            for i in range(0, len(portfolio1)):
                income_ave = 0
                income_size = 0
                for number in range(0, len(portfolio1[i])):
                    if "t" + portfolio1[i][number] + "d" + data_date[t] in data_stocks_dic.keys():
                        if math.isnan(data_stocks_dic["t" + portfolio1[i][number] + "d" + data_date[t]]) != True:
                            portfolio_by_size[i][number] = portfolio_by_size[i][number] * ( data_stocks_dic["t" + portfolio1[i][number] + "d" + data_date[t]] + 1)
                            portfolio_by_average[i][number] = portfolio_by_average[i][number] * ( data_stocks_dic["t" + portfolio1[i][number] + "d" + data_date[t]] + 1)
                            income_ave = income_ave + (portfolio_by_average1[i][number] * data_stocks_dic["t" + portfolio1[i][number] + "d" + data_date[t]])*100000
                            income_size = income_size + (portfolio_by_size1[i][number] * data_stocks_dic["t" + portfolio1[i][number] + "d" + data_date[t]])*100000

                basket_size.append(income_size/100000)
                basket_ave.append(income_ave/100000)

            monthly_return_ave.append(basket_ave)
            monthly_return_size.append(basket_size)

            if t % self.T == self.start_date % self.T - 1:
                for i in range(0, len(portfolio_by_average)):
                    portfolio_return_by_average[i].append((sum(portfolio_by_average[i])-1) / self.T )

                for i in range(0, len(portfolio_by_size)):
                    portfolio_return_by_size[i].append((sum(portfolio_by_size[i])-1) / self.T )

        return portfolio_return_by_average, portfolio_return_by_size, monthly_return_ave, monthly_return_size