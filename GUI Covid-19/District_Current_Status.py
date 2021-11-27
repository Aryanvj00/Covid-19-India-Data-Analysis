import pandas as pd
import matplotlib.pyplot as plt

def district_Current_Status(district,district_wise):
    ########## Getting the Required Data ###########
    data = district_wise.copy()
    Active = int(data[data['District'] == district].Active)
    Confirmed = int(data[data['District'] == district].Confirmed)
    Deaths = int(data[data['District'] == district].Deceased)
    Recovered = int(data[data['District'] == district].Recovered)

    pie_data = [Active/Confirmed*100, Recovered/Confirmed*100, Deaths/Confirmed*100]
    bar_data = [Confirmed ,Active, Recovered, Deaths]
    label = ["Confirmed","Active", "Recovered", "Deaths"]

    ########## Pie Plot #########################
    plt.figure(district +" Current Status")
    labels = [f'{l}, {s:0.2f}%' for l, s in zip(label, pie_data)]
    plt.pie(pie_data, labels = labels, explode = (0.1, 0.1, 0.1))
    plt.title(district +" Current Status")
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    plt.show()

    ########## Bar Plot #########################
    plt.figure(district +" Current Status" + " Bar plot")
    plt.bar('Confirmed', Confirmed)
    plt.bar('Active', Active)
    plt.bar('Recovered', Recovered)
    plt.bar('Deaths', Deaths)
    labels = [f'{l}, {s:}' for l, s in zip(label, bar_data)]
    plt.legend(bbox_to_anchor=(0.75, 1), loc='upper left', labels=labels)

    
    plt.title(district +" Current Status")
    plt.ylabel('Number of People')
    plt.text('Confirmed', Confirmed, str(Confirmed))
    plt.text('Active', Active, str(Active))
    plt.text('Recovered', Recovered, str(Recovered))
    plt.text('Deaths', Deaths, str(Deaths))
    plt.show()