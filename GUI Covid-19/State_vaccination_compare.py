from os import stat
import matplotlib.pyplot as plt
import pandas as pd

def state_vaccination_compare(state1, state2, state3):
    state_vaccine_15days = pd.read_csv("vaccine_doses_statewise_v2.csv")
    state = [state1, state2, state3]
    date = state_vaccine_15days[state_vaccine_15days['State'] == state[0]].Date
    date = date.tail(15)

    # for state 1 :
    total_dose_1 = state_vaccine_15days[state_vaccine_15days['State'] == state[0]].total_doses
    total_dose_1 = total_dose_1.tail(15)
    date_1 = state_vaccine_15days[state_vaccine_15days['State'] == state[0]].Date
    date_1 = date_1.tail(15)

    # for state 2:
    total_dose_2 = state_vaccine_15days[state_vaccine_15days['State'] == state[1]].total_doses
    total_dose_2 = total_dose_2.tail(15)
    date_2 = state_vaccine_15days[state_vaccine_15days['State'] == state[1]].Date
    date_2 = date_2.tail(15)

    # for state 3:
    total_dose_3 = state_vaccine_15days[state_vaccine_15days['State'] == state[2]].total_doses
    total_dose_3 = total_dose_3.tail(15)
    date_3 = state_vaccine_15days[state_vaccine_15days['State'] == state[2]].Date
    date_3 = date_3.tail(15)

    plt.figure("Comparison on Confirmed Cases in Last 15 days")
    plt.rc('xtick', labelsize=8)
    plt.rc('ytick', labelsize=8)
    plt.plot(date, total_dose_1, marker='o')
    plt.plot(date, total_dose_2, marker='o')
    plt.plot(date, total_dose_3, marker='o')
    plt.title('Comparison on Confirmed Cases in Last 15 days')
    plt.legend([state[0],state[1],state[2]])
    for a, b in zip(date, total_dose_1):
        plt.text(a, b, str(b))
    for a, b in zip(date, total_dose_2):
        plt.text(a, b, str(b))
    for a, b in zip(date, total_dose_3):
        plt.text(a, b, str(b))
    plt.xlabel('Date')
    plt.ylabel('Number of people')
    plt.show()

