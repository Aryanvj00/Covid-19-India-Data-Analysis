import matplotlib.pyplot as plt
import pandas as pd

def state_vaccine_daily(state):
    state_vaccine_15days = pd.read_csv("vaccine_doses_statewise_v2.csv")

    total_dose = state_vaccine_15days[state_vaccine_15days['State'] == state].total_doses
    total_dose = total_dose.tail(15)
    date = state_vaccine_15days[state_vaccine_15days['State'] == state].Date
    date = date.tail(15)

    plt.figure('Vaccination in' + state + ' Last 15 days')
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, total_dose, marker='o')
    plt.title('Vaccination in' + state + ' Last 15 days')
    plt.legend(state)
    for a, b in zip(date, total_dose):
        plt.text(a, b, str(b))
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.show()
