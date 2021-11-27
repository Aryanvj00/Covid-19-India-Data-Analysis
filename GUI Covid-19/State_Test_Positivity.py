import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def state_Test_Positivity(state,statewise_tested_number_data,state_wise,state_wise_daily):
    ################ Getting the required Data ################
    data = statewise_tested_number_data.copy()
    data_1 = state_wise.copy()
    data_2 = state_wise_daily.copy()
    data.rename(columns={"Total Tested": "TotalTested"}, inplace=True)
    data.rename(columns={"Updated On": "Date"}, inplace=True)
    daily_Tested = -((data[data['State'] == state].tail(17).TotalTested) - (data[data['State'] == state].tail(17).TotalTested.shift(-1)))
    daily_Tested=daily_Tested[:-2]
    data_1 = state_wise.copy()
    data_1["State_code"] = data_1["State_code"].astype(str)
    state_Code = data_1[data_1['State'] == state].State_code
    temp = []
    for i in state_Code:
        temp.append(i)
    code = ''.join([str(elem) for elem in temp])
    data_2 = state_wise_daily.copy()
    data_2.rename(columns={code: "code"}, inplace=True)
    daily_Confirmed = data_2[data_2['Status'] == 'Confirmed'].tail(15).code
    date=data[data['State'] == state].tail(16).Date
    date=date[:-1]
    rate = np.round(((np.array(daily_Confirmed)/np.array(daily_Tested))*100),2)

    ############# Line Plot ################################
    title = state + ": Last 15 days Testing to Corresponding Positive Count"
    plt.figure(title)
    plt.plot(date, daily_Tested, marker='o')
    plt.plot(date, daily_Confirmed, marker='o')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.title(title)
    plt.xlabel('Date')
    plt.legend(["Daily Tested", "Daily Positive"],loc = 'upper left')
    for a, b in zip(date, daily_Tested):
        plt.text(a, b, str(b))
    for a, b in zip(date, daily_Confirmed):
        plt.text(a, b, str(b))
    plt.show()

    ###################### Line Plot #####################
    title = state + ": Test Positivity Rate in Last 15 Days"
    plt.figure(title)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, rate, marker='o')
    plt.legend(["Rate"],loc = 'upper left')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('%Rate')
    for a, b in zip(date, rate):
        plt.text(a, b, str(b))
    plt.show()
