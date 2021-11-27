import matplotlib.pyplot as plt
import pandas as pd

def india_Current_Status(state_wise):
    ############## Getting the Required Data   #########
    data = state_wise.copy()
    Active = int(data[data['State_code'] == 'TT'].Active)
    Recovered = int(data[data['State_code'] == 'TT'].Recovered)
    Deaths = int(data[data['State_code'] == 'TT'].Deaths)
    Confirmed = int(data[data['State_code'] == 'TT'].Confirmed)

    pie_data = [Active/Confirmed*100, Recovered/Confirmed*100, Deaths/Confirmed*100]
    bar_data = [Confirmed,Active, Recovered, Deaths]
    label = ["Active", "Recovered", "Deaths"]

    ########## Pie Plot #########################
    labels = [f'{l}, {s:0.2f}%' for l, s in zip(label, pie_data)]
    plt.figure("India Current Status")
    plt.pie(pie_data, labels = labels, explode = (0.1, 0.1, 0.1))
    plt.title("India Current Status")
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    plt.show()

    ########## Bar Plot #########################
    label = ["Confirmed", "Active", "Recovered", "Deaths"]
    plt.figure("India Current Status Bar Plot")
    plt.bar('Confirmed', Confirmed)
    plt.bar('Active', Active)
    plt.bar('Recovered', Recovered)
    plt.bar('Deaths', Deaths)
    labels = [f'{l}, {s:}' for l, s in zip(label, bar_data)]
    plt.legend(bbox_to_anchor=(0.9, 1), loc='upper left', labels=labels)
    plt.title("India Current Status")
    plt.ylabel('Number of People')
    plt.text('Confirmed', Confirmed, str(Confirmed))
    plt.text('Active', Active, str(Active))
    plt.text('Recovered', Recovered, str(Recovered))
    plt.text('Deaths', Deaths, str(Deaths))
    plt.show()
