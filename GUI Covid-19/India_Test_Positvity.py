import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def india_Test_Positivity(tested_number_icmr_data,case_time_series):
    ########### Getting the required Data ###############
    data = tested_number_icmr_data.copy()
    data_1 = case_time_series.copy()
    daily_Tested = -(data['Total Samples Tested'].tail(16) - data['Total Samples Tested'].tail(16).shift(-1))
    daily_Tested = pd.to_numeric(daily_Tested[:-1],downcast="integer")
    daily_Confirmed=data_1['Daily Confirmed'].tail(15)
    date = pd.to_datetime(data_1['Date'].tail(15))

    ############ Line Plot ###################
    plt.figure('Last 15 days Testing to Corresponding Positive Count')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, daily_Tested, marker='o')
    plt.plot(date, daily_Confirmed, marker='o')
    plt.xlabel('Date')
    plt.ylabel('Count')
    plt.yticks(color='w') # hiding y ticks
    plt.title('Last 15 days Testing to Corresponding Positive Count')
    plt.legend(["Daily Test Count", "Daily Positive Cases"])
    plt.grid(True)
    for a, b in zip(date, daily_Tested):
        plt.text(a, b, str(b))
    for a, b in zip(date, daily_Confirmed):
        plt.text(a, b, str(b))
    plt.show()

    ############ Line Plot ###################
    plt.figure('Test Positivity Rate in Last 15 Days')
    rate = np.round(((np.array(daily_Confirmed)/np.array(daily_Tested))*100),2)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, rate, marker='o')
    plt.title('Test Positivity Rate in Last 15 Days')
    plt.xlabel('Date')
    plt.ylabel('%Rate')
    plt.legend(["Test Positive Rate"])
    plt.grid(True)
    for a, b in zip(date, rate):
        plt.text(a, b, str(b))
    plt.show()