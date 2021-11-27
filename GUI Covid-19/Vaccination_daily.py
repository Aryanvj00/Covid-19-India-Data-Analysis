import pandas as pd
import matplotlib.pyplot as plt

def vaccination_daily(india_vaccine):
    india_15day_vaccine = india_vaccine.copy()
    Covaxin=india_15day_vaccine["Covaxin (Doses Administered)"].tail(15)
    Covishield=india_15day_vaccine["CoviShield (Doses Administered)"].tail(15)
    Sputnik=india_15day_vaccine["Sputnik V (Doses Administered)"].tail(15)
    date = india_15day_vaccine['date'].tail(15)

    title = "Vaccination Last 15 days status"
    plt.figure(title)
    plt.rcParams["figure.figsize"] = (15, 8)
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date,Covaxin, marker='o')
    plt.plot(date,Covishield, marker='o')
    plt.plot(date,Sputnik, marker='o')
    plt.legend(["Covaxin Vaccinated","Covishield Vaccinated", "Sputnik Vaccinated"])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('number of  people')
    for a, b in zip(date, Covaxin):
        plt.text(a, b, str(b))
    for a, b in zip(date, Covishield):
        plt.text(a, b, str(b))
    for a, b in zip(date, Sputnik):
        plt.text(a, b, str(b))
    plt.show()