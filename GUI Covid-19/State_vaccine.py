import matplotlib.pyplot as plt
import pandas as pd
from pandas.tseries.offsets import CBMonthBegin

def state_vaccine(state,vaccine_state_wise):
    vaccine_statewise = vaccine_state_wise.copy()
    vaccine_statewise.rename(columns = {'Updated On':'date','Covaxin (Doses Administered)':'covaxin_doses','CoviShield (Doses Administered)':'covishield_doses','Sputnik V (Doses Administered)':'sputnik_doses','Male (Individuals Vaccinated)':'males_vaccinated','Female (Individuals Vaccinated)':'female_vaccinate','Transgender (Individuals Vaccinated)':'other_doses'}, inplace = True)
    Covaxin = vaccine_statewise[vaccine_statewise['State'] == state].covaxin_doses
    Covishield=vaccine_statewise[vaccine_statewise['State'] == state].covishield_doses
    Sputnik=vaccine_statewise[vaccine_statewise['State'] == state].sputnik_doses

    pie_data = [Covaxin.max(), Covishield.max(), Sputnik.max()]
    label=["Covaxin Vaccinated","Covishield Vaccinated", "Sputnik Vaccinated"]

    plt.figure(state + " Vaccination Current Status" + "Pie chart")
    plt.pie(pie_data, labels = label,autopct='%1.1f%%')
    plt.axis('equal')
    plt.title(state + " Vaccination Current Status")
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=label)
    plt.show()

    Covaxin = Covaxin.max()
    Covishield = Covishield.max()
    Sputnik = Sputnik.max()


    plt.figure(state + " Vaccination Current Status" + "Bar plot")
    plt.bar('Covaxin Vaccinated', Covaxin)
    plt.bar('Covishield', Covishield)
    plt.bar('Sputnik', Sputnik)
    labels = [f'{l}, {s:}' for l, s in zip(label, pie_data)]
    plt.legend(bbox_to_anchor=(0.8, 1), loc='upper left', labels=labels)
    plt.title(state + " Vaccination Current Status")
    plt.ylabel('Number of People')
    plt.text('Covaxin Vaccinated', Covaxin, str(Covaxin))
    plt.text('Covishield Vaccinated', Covishield, str(Covishield))
    plt.text('Sputnik Vaccinated', Sputnik, str(Sputnik))
    plt.show()