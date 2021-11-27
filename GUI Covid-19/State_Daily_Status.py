import matplotlib.pyplot as plt
import pandas as pd

def state_Daily_Status(state,state_wise,state_wise_daily):
    ########### Getting the required Data ###############
    data = state_wise.copy()
    data["State_code"] = data["State_code"].astype(str)
    state_Code = data[data['State'] == state].State_code
    temp = []
    for i in state_Code:
        temp.append(i)
    code = ''.join([str(elem) for elem in temp])
    data = state_wise_daily.copy()
    data.rename(columns={code: "code"}, inplace=True)
    Confirmed = data[data['Status'] == 'Confirmed'].tail(
        15).code
    Recovered = data[data['Status'] == 'Recovered'].tail(
        15).code
    Deaths = data[data['Status'] == 'Deceased'].tail(15).code
    date=pd.to_datetime(data[data['Status'] == 'Confirmed'].tail(
            15).Date)

    ############## Line Plot #################
    title = (state + ': Last 15 Day Status')
    plt.figure(title)
    plt.rcParams["figure.figsize"] = (15, 8)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, Confirmed, marker='o')
    plt.plot(date, Recovered, marker='o')
    plt.plot(date, Deaths, marker='o')
    plt.legend(["Confirmed", "Recovered", "Deceased"])
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.grid(True)
    plt.title(title)
    for a, b in zip(date, Confirmed):
        plt.text(a, b, str(b))
    for a, b in zip(date, Recovered):
        plt.text(a, b, str(b))
    for a, b in zip(date, Deaths):
        plt.text(a, b, str(b))
    plt.show()