import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def state_Compare(state_1,state_2,state_3,state_wise,state_wise_daily,statewise_tested_number_data):
    ################ Getting the required Data ##############
    state = [state_1,state_2,state_3]
    data = state_wise.copy()
    data["State_code"] = data["State_code"].astype(str)
    code = []
    for i in state:
        state_Code = data[data['State'] == i].State_code
        temp = []
        for i in state_Code:
            temp.append(i)
        code.append(''.join([str(elem) for elem in temp]))
    data = state_wise_daily.copy()
    data_1 = statewise_tested_number_data.copy()
    data_1.rename(columns={"Total Tested": "TotalTested"}, inplace=True)
    data_1.rename(columns={"Updated On": "Date"}, inplace=True)
    date=data_1[data_1['State'] == state[0]].tail(16).Date
    date=date[:-1]

    ####### state_1 ####################
    data.rename(columns={code[0]: 'state_1'}, inplace=True)
    state_1_Confirmed = data[data['Status'] == 'Confirmed'].tail(15).state_1
    state_1_Recovered = data[data['Status'] == 'Recovered'].tail(15).state_1
    state_1_Deceased = data[data['Status'] == 'Deceased'].tail(15).state_1
    state_1_Tested = -((data_1[data_1['State'] == state[0]].tail(17).TotalTested) - (data_1[data_1['State'] == state[0]].tail(17).TotalTested.shift(-1)))
    state_1_Tested = state_1_Tested[:-2]
    state_1_Rate = np.round(((np.array(state_1_Confirmed)/np.array(state_1_Tested))*100),2)

    ####### state_2 ####################
    data.rename(columns={code[1]: 'state_2'}, inplace=True)
    state_2_Confirmed = data[data['Status'] == 'Confirmed'].tail(15).state_2
    state_2_Recovered = data[data['Status'] == 'Recovered'].tail(15).state_2
    state_2_Deceased = data[data['Status'] == 'Deceased'].tail(15).state_2
    state_2_Tested = -((data_1[data_1['State'] == state[1]].tail(17).TotalTested) - (data_1[data_1['State'] == state[1]].tail(17).TotalTested.shift(-1)))
    state_2_Tested = state_2_Tested[:-2]
    state_2_Rate = np.round(((np.array(state_2_Confirmed)/np.array(state_2_Tested))*100),2)

    ####### state_3 ####################
    data.rename(columns={code[2]: 'state_3'}, inplace=True)
    state_3_Confirmed = data[data['Status'] == 'Confirmed'].tail(15).state_3
    state_3_Recovered = data[data['Status'] == 'Recovered'].tail(15).state_3
    state_3_Deceased = data[data['Status'] == 'Deceased'].tail(15).state_3
    state_3_Tested = -((data_1[data_1['State'] == state[2]].tail(17).TotalTested) - (data_1[data_1['State'] == state[2]].tail(17).TotalTested.shift(-1)))
    state_3_Tested = state_3_Tested[:-2]
    state_3_Rate = np.round(((np.array(state_3_Confirmed)/np.array(state_3_Tested))*100),2)

    ####### line plot Confirmed ####################
    plt.figure('Comparison on Confirmed Cases in Last 15 days')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, state_1_Confirmed, marker='o')
    plt.plot(date, state_2_Confirmed, marker='o')
    plt.plot(date, state_3_Confirmed, marker='o')
    plt.title('Comparison on Confirmed Cases in Last 15 days')
    plt.legend([state[0],state[1],state[2]])
    for a, b in zip(date, state_1_Confirmed):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_2_Confirmed):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_3_Confirmed):
        plt.text(a, b, str(b))
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.show()

    ####### line plot Recovered ####################
    plt.figure('Comparison on Recovered Cases in Last 15 days')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, state_1_Recovered, marker='o')
    plt.plot(date, state_2_Recovered, marker='o')
    plt.plot(date, state_3_Recovered, marker='o')
    plt.title('Comparison on Recovered Cases in Last 15 days')
    plt.legend([state[0],state[1],state[2]])
    for a, b in zip(date, state_1_Recovered):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_2_Recovered):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_3_Recovered):
        plt.text(a, b, str(b))
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.show()

    ####### line plot Deceased ####################
    plt.figure('Comparison on Deceased Cases in Last 15 days')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, state_1_Deceased, marker='o')
    plt.plot(date, state_2_Deceased, marker='o')
    plt.plot(date, state_3_Deceased, marker='o')
    plt.title('Comparison on Deceased Cases in Last 15 days')
    plt.legend([state[0],state[1],state[2]])
    for a, b in zip(date, state_1_Deceased):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_2_Deceased):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_3_Deceased):
        plt.text(a, b, str(b))
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.show()

    ####### line plot test positivity ####################
    plt.figure('Comparison on test positivity in Last 15 days')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, state_1_Rate, marker='o')
    plt.plot(date, state_2_Rate, marker='o')
    plt.plot(date, state_3_Rate, marker='o')
    plt.title('Comparison on test positivity in Last 15 days')
    plt.legend([state[0],state[1],state[2]])
    for a, b in zip(date, state_1_Rate):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_2_Rate):
        plt.text(a, b, str(b))
    for a, b in zip(date, state_3_Rate):
        plt.text(a, b, str(b))
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.show()