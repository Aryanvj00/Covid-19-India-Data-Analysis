import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import plotly.express as px

def vaccination_total(vaccine_state_wise):
    vaccine_data=vaccine_state_wise.copy()

    male = vaccine_data["Male (Individuals Vaccinated)"].max() 
    female = vaccine_data["Female (Individuals Vaccinated)"].max()  
    other = vaccine_data["Transgender (Individuals Vaccinated)"].max()

    pie_data=[male,female,other]
    label=["Male Vaccinated","Female Vaccinated", "Other Vaccinated"]

    plt.figure("Vaccination By Gender")
    plt.pie(pie_data, labels = label,autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Vaccination")
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=label)
    plt.show()
    
    bar_data = [male, female, other]
    label=["Male Vaccinated","Female Vaccinated", "Other Vaccinated"]
    
    plt.figure("Vaccinated By Gender Bar Plot")
    plt.bar('Males Vaccinated', male)
    plt.bar('Females Vaccinated', female)
    plt.bar('Others Vaccinated', other)
    labels = [f'{l}, {s:}' for l, s in zip(label, bar_data)]
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left', labels=labels)
    plt.title("India Vaccination Current Status")
    plt.ylabel('Number of People')
    plt.text('Males Vaccinated', male, str(male))
    plt.text('Female Vaccinated', female, str(female))
    plt.text('Other Vaccinated', other, str(other))
    plt.show()
    
    Covaxin=vaccine_data["Covaxin (Doses Administered)"].max() 
    Covishield=vaccine_data["CoviShield (Doses Administered)"].max()  
    Sputnik=vaccine_data["Sputnik V (Doses Administered)"].max()

    
    pie_data=[Covaxin,Covishield,Sputnik]
    label=["Covaxin Vaccinated","Covishield Vaccinated", "Sputnik Vaccinated"]
    # labels = [f'{l}, {s:100.02f}%' for l, s in zip(label, pie_data)]
    plt.figure("Vaccines Used")
    plt.pie(pie_data, labels = label,autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Vaccination")
    plt.legend(bbox_to_anchor=(0.85, 1), loc='upper left', labels=label)
    plt.show()

    plt.figure("India Vaccination Current Status")
    plt.bar('Covaxin Vaccinated', Covaxin)
    plt.bar('Covishield', Covishield)
    plt.bar('Sputnik', Sputnik)
    labels = [f'{l}, {s:}' for l, s in zip(label, pie_data)]
    plt.legend(bbox_to_anchor=(1.1, 1), loc='upper left', labels=labels)
    plt.title("India Vaccination Current Status")
    plt.ylabel('Number of People')
    plt.text('Covaxin Vaccinated', Covaxin, str(Covaxin))
    plt.text('Covishield', Covishield, str(Covishield))
    plt.text('Sputnik', Sputnik, str(Sputnik))
    plt.show()
