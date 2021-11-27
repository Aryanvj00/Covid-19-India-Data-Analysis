
import pandas as pd

def state_Current_Status(state,state_wise):
    ########### Getting the required Data ################
    
    data = state_wise.copy()
    Active = int(data[data['State'] == state].Active)
    Recovered = int(data[data['State'] == state].Recovered)
    Deaths = int(data[data['State'] == state].Deaths)
    Confirmed = int(data[data['State'] == state].Confirmed)

    pie_data = [Active/Confirmed*100, Recovered/Confirmed*100, Deaths/Confirmed*100]
    label = ["Active", "Recovered", "Deaths"]

    ############## Pie Plot ##################
    import matplotlib.pyplot as plt
    plt.figure(state + " Current Status")
    labels = [f'{l}, {s:0.2f}%' for l, s in zip(label, pie_data)]
    plt.pie(pie_data, labels = labels, explode = (0.1, 0.1, 0.1))
    plt.title(state + " Current Status")
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=labels)
    plt.show()

    ############ Bar Plot #########################
    bar_data = [Confirmed, Active, Recovered, Deaths]
    label = ["Confirmed", "Active", "Recovered", "Deaths"]
    import matplotlib.pyplot as plt
    plt.figure("" + state + " Current Status" + "Bar Plot")
    plt.bar('Confirmed', Confirmed)
    plt.bar('Active', Active)
    plt.bar('Recovered', Recovered)
    plt.bar('Deaths', Deaths)
    labels = [f'{l}, {s:}' for l, s in zip(label, bar_data)]
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', labels=labels)
    plt.title(state + " Current Status")
    plt.ylabel('Number of People')
    plt.text('Confirmed', Confirmed, str(Confirmed))
    plt.text('Active', Active, str(Active))
    plt.text('Recovered', Recovered, str(Recovered))
    plt.text('Deaths', Deaths, str(Deaths))
    plt.show()