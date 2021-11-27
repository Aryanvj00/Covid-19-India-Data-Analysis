import matplotlib.pyplot as plt
import pandas as pd

def india_Daily_Status(case_time_series):
    ########## Getting the Required Data ########## 
    data = case_time_series.copy()
    Daily_Confirmed=data['Daily Confirmed'].tail(15)
    Daily_Recovered=data['Daily Recovered'].tail(15)
    Daily_Deceased=data['Daily Deceased'].tail(15)
    date = pd.to_datetime(data['Date'].tail(15))

    ########## Line Plot ########## 
    plt.figure("Last 15 daily days Status")
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, Daily_Confirmed, marker='o')
    plt.plot(date, Daily_Recovered, marker='o')
    plt.plot(date, Daily_Deceased, marker='o')
    plt.title("Last 15 daily days Status")
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.legend(["Confirmed", "Recovered", "Deceased"])
    plt.grid(True)
    for a, b in zip(date, Daily_Confirmed):
        plt.text(a, b, str(b))
    for a, b in zip(date, Daily_Recovered):
        plt.text(a, b, str(b))
    for a, b in zip(date, Daily_Deceased):
        plt.text(a, b, str(b))
    plt.show()