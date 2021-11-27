import pandas as pd
import matplotlib.pyplot as plt

def district_Daily_Status(district,districts):
    #################### Getting the Data ###############
    data = districts.copy()
    daily_Confirmed = -(data[data['District']==district].tail(16).Confirmed - data[data['District']==district].tail(16).Confirmed.shift(-1))
    daily_Confirmed=pd.to_numeric(daily_Confirmed[:-1],downcast="integer")
    daily_Recovered = -(data[data['District']==district].tail(16).Recovered - data[data['District']==district].tail(16).Recovered.shift(-1))
    daily_Recovered=pd.to_numeric(daily_Recovered[:-1],downcast="integer")
    daily_Deaths = -(data[data['District']==district].tail(16).Deceased - data[data['District']==district].tail(16).Deceased.shift(-1))
    daily_Deaths =pd.to_numeric(daily_Deaths[:-1],downcast="integer")
    date=data[data['District']==district].tail(15).Date

    ################## Line plot ####################
    plt.figure(district + ": Last 15 days status")
    plt.rcParams["figure.figsize"] = (15, 8)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date,daily_Confirmed, marker='o')
    plt.plot(date,daily_Recovered, marker='o')
    plt.plot(date,daily_Deaths, marker='o')
    plt.legend(["daily_Confirmed","daily_Recovered",'daily_Deaths'])
    plt.title(district + ": Last 15 days status")
    plt.xlabel('Date')
    plt.ylabel('number of  people')
    for a, b in zip(date, daily_Confirmed):
        plt.text(a, b, str(b))
    for a, b in zip(date, daily_Recovered):
        plt.text(a, b, str(b))
    for a, b in zip(date, daily_Deaths):
        plt.text(a, b, str(b))
    plt.show()