##### Libraries imported #######
from PyQt5 import QtCore, QtGui, QtWidgets, QtWidgets
import sys
from PyQt5.QtWidgets import * 
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.sip import *
import pandas as pd

######## Required files import ##########
from India_Current_Status import india_Current_Status
from India_Daily_Status import india_Daily_Status
from India_Test_Positvity import india_Test_Positivity
from State_Current_Status import state_Current_Status
from State_Daily_Status import state_Daily_Status
from State_Test_Positivity import state_Test_Positivity
from State_Comparison import state_Compare
from District_Current_Status import district_Current_Status
from District_Daily_Status import district_Daily_Status
from State_vaccine import state_vaccine
from State_vaccine_daily import state_vaccine_daily
from Vaccination_total import vaccination_total
from Vaccination_daily import vaccination_daily
from State_vaccination_compare import state_vaccination_compare


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)


class Ui_Covid_Analysis(QWidget):
    def setupUi(self, Covid_Analysis):
        Covid_Analysis.setObjectName(_fromUtf8("Covid_Analysis"))
        Covid_Analysis.resize(700, 550)
        Covid_Analysis.setAutoFillBackground(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("data\icon.ico")),QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Covid_Analysis.setWindowIcon(icon)
        self.line = QtWidgets.QFrame(Covid_Analysis)
        self.line.setGeometry(QtCore.QRect(0, 170, 701, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtWidgets.QFrame(Covid_Analysis)
        self.line_2.setGeometry(QtCore.QRect(0, 450, 701, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtWidgets.QFrame(Covid_Analysis)
        self.line_3.setGeometry(QtCore.QRect(0, 45, 701, 20))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtWidgets.QFrame(Covid_Analysis)
        self.line_4.setGeometry(QtCore.QRect(0, 315, 701, 20))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_India = QtWidgets.QLabel(Covid_Analysis)
        self.label_India.setGeometry(QtCore.QRect(270, 70, 211, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_India.setFont(font)
        self.label_India.setObjectName(_fromUtf8("label_India"))
        self.label_State = QtWidgets.QLabel(Covid_Analysis)
        self.label_State.setGeometry(QtCore.QRect(270, 194, 191, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_State.setFont(font)
        self.label_State.setObjectName(_fromUtf8("label_State"))
        self.label_State_comparison = QtWidgets.QLabel(Covid_Analysis)
        self.label_State_comparison.setGeometry(QtCore.QRect(270, 335, 191, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_State_comparison.setFont(font)
        self.label_State_comparison.setObjectName(_fromUtf8("label_State_comparison"))
        self.label_District = QtWidgets.QLabel(Covid_Analysis)
        self.label_District.setGeometry(QtCore.QRect(270, 470, 211, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_District.setObjectName(_fromUtf8("label_District"))
        self.label_District.setFont(font)
        self.progressBar = QtWidgets.QProgressBar(Covid_Analysis)
        self.progressBar.setGeometry(QtCore.QRect(100, 20, 151, 21))
        self.progressBar.setMinimum(0)
        self.progressBar.setRange(0, 100)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.Button_GetData = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_GetData.setGeometry(QtCore.QRect(300, 20, 111, 23))
        self.Button_GetData.setObjectName(_fromUtf8("Button_GetData"))
        self.Button_GetData.clicked.connect(self.get_Required_Data)
        self.Button_IndiaCurrent = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaCurrent.setGeometry(QtCore.QRect(60, 100, 111, 23))
        self.Button_IndiaCurrent.setObjectName(_fromUtf8("Button_IndiaCurrent"))
        self.Button_IndiaCurrent.setEnabled(False)
        self.Button_IndiaCurrent.clicked.connect(self.India_Current_Status)
        self.Button_IndiaDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaDaily.setGeometry(QtCore.QRect(270, 100, 125, 23))
        self.Button_IndiaDaily.setObjectName(_fromUtf8("Button_IndiaDaily"))
        self.Button_IndiaDaily.setEnabled(False)
        self.Button_IndiaDaily.clicked.connect(self.India_Daily_Status)
        self.Button_IndiaPositivity = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaPositivity.setGeometry(QtCore.QRect(460, 100, 200, 23))
        self.Button_IndiaPositivity.setObjectName(_fromUtf8("Button_IndiaPositivity"))
        self.Button_IndiaPositivity.setEnabled(False)
        self.Button_IndiaPositivity.clicked.connect(self.India_Test_Positivity)
        self.Button_IndiaVaccine = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_IndiaVaccine.setGeometry(QtCore.QRect(150, 140, 125, 23))
        self.Button_IndiaVaccine.setObjectName(_fromUtf8("Button_IndiaVaccination"))
        self.Button_IndiaVaccine.setEnabled(False)
        self.Button_IndiaVaccine.clicked.connect(self.Vaccination_total)
        self.Button_VaccineDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_VaccineDaily.setGeometry(QtCore.QRect(380, 140, 200, 23))
        self.Button_VaccineDaily.setObjectName(_fromUtf8("Button_VaccinationDaily"))
        self.Button_VaccineDaily.setEnabled(False)
        self.Button_VaccineDaily.clicked.connect(self.Vaccination_daily)
        self.Button_StateCurrent = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_StateCurrent.setGeometry(QtCore.QRect(180, 230, 101, 23))
        self.Button_StateCurrent.setObjectName(_fromUtf8("Button_StateCurrent"))
        self.Button_StateCurrent.setEnabled(False)
        self.Button_StateCurrent.clicked.connect(self.State_Current_Status)
        self.Button_StateDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_StateDaily.setGeometry(QtCore.QRect(315, 230, 121, 23))
        self.Button_StateDaily.setObjectName(_fromUtf8("Button_StateDaily"))
        self.Button_StateDaily.setEnabled(False)
        self.Button_StateDaily.clicked.connect(self.State_Daily_Status)
        self.Button_StatePositivity = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_StatePositivity.setGeometry(QtCore.QRect(465, 230, 201, 23))
        self.Button_StatePositivity.setObjectName(_fromUtf8("Button_StatePositivity"))
        self.Button_StatePositivity.setEnabled(False)
        self.Button_StatePositivity.clicked.connect(self.State_Test_Positivity)
        self.Button_State_vaccine = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_State_vaccine.setGeometry(QtCore.QRect(200, 280, 121, 22))
        self.Button_State_vaccine.setObjectName(_fromUtf8("Button_State_vaccine"))
        self.Button_State_vaccine.setEnabled(False)
        self.Button_State_vaccine.clicked.connect(self.State_vaccine)
        self.Button_State_vaccine_daily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_State_vaccine_daily.setGeometry(QtCore.QRect(360, 280, 160, 22))
        self.Button_State_vaccine_daily.setObjectName(_fromUtf8("Button_State_vaccine"))
        self.Button_State_vaccine_daily.setEnabled(False)
        self.Button_State_vaccine_daily.clicked.connect(self.State_vaccine_daily)
        self.Button_State_vaccination_compare = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_State_vaccination_compare.setGeometry(QtCore.QRect(370, 415, 180, 23))
        self.Button_State_vaccination_compare.setObjectName(_fromUtf8("Button_Compare"))
        self.Button_State_vaccination_compare.setEnabled(False)
        self.Button_State_vaccination_compare.clicked.connect(self.State_vaccination_compare)      
        self.Button_Compare = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_Compare.setGeometry(QtCore.QRect(140, 415, 180, 23))
        self.Button_Compare.setObjectName(_fromUtf8("Button_Compare"))
        self.Button_Compare.setEnabled(False)
        self.Button_Compare.clicked.connect(self.State_Comparision)
        self.Button_DistrictStatus = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_DistrictStatus.setGeometry(QtCore.QRect(270, 505, 150, 23))
        self.Button_DistrictStatus.setObjectName(_fromUtf8("Button_DistrictStatus"))
        self.Button_DistrictStatus.setEnabled(False)
        self.Button_DistrictStatus.clicked.connect(self.District_Current_Status)
        self.Button_DistrictDaily = QtWidgets.QPushButton(Covid_Analysis)
        self.Button_DistrictDaily.setGeometry(QtCore.QRect(470, 505, 150, 23))
        self.Button_DistrictDaily.setObjectName(_fromUtf8("Button_DistrictDaily"))
        self.Button_DistrictDaily.setEnabled(False)
        self.Button_DistrictDaily.clicked.connect(self.District_Daily_Status)
        self.comboBox_State = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_State.setGeometry(QtCore.QRect(20, 230, 121, 22))
        self.comboBox_State.setEditable(False)
        self.comboBox_State.setMaxVisibleItems(13)
        self.comboBox_State.setObjectName(_fromUtf8("comboBox_State"))
        self.comboBox_State.addItem(_fromUtf8(""))
        self.comboBox_State_vaccine = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_State_vaccine.setGeometry(QtCore.QRect(20, 280, 121, 22))
        self.comboBox_State_vaccine.setEditable(False)
        self.comboBox_State_vaccine.setMaxVisibleItems(13)
        self.comboBox_State_vaccine.setObjectName(_fromUtf8("comboBox_State"))
        self.comboBox_State_vaccine.addItem(_fromUtf8(""))
        self.comboBox_Compare_1 = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_Compare_1.setGeometry(QtCore.QRect(70, 370, 150, 22))
        self.comboBox_Compare_1.setObjectName(_fromUtf8("comboBox_Compare_1"))
        self.comboBox_Compare_1.addItem(_fromUtf8(""))
        self.comboBox_Compare_2 = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_Compare_2.setGeometry(QtCore.QRect(280, 370, 150, 22))
        self.comboBox_Compare_2.setObjectName(_fromUtf8("comboBox_Compare_2"))
        self.comboBox_Compare_2.addItem(_fromUtf8(""))
        self.comboBox_Compare_3 = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_Compare_3.setGeometry(QtCore.QRect(480, 370, 150, 22))
        self.comboBox_Compare_3.setObjectName(_fromUtf8("comboBox_Compare_3"))
        self.comboBox_Compare_3.addItem(_fromUtf8(""))
        self.comboBox_District = QtWidgets.QComboBox(Covid_Analysis)
        self.comboBox_District.setGeometry(QtCore.QRect(70, 505, 150, 22))
        self.comboBox_District.setObjectName(_fromUtf8("comboBox_District"))
        self.comboBox_District.addItem(_fromUtf8(""))
        self.retranslateUi(Covid_Analysis)
        self.comboBox_State.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Covid_Analysis)

    def get_Required_Data(self):
        global state_wise
        global case_time_series
        global tested_number_icmr_data
        global state_wise_daily
        global statewise_tested_number_data
        global vaccine_state_wise
        global district_wise
        global districts
        global india_vaccine
        global vaccine_state

        ########## Reading the Data ##########################
        try:
            # state_wise = pd.read_csv(
                # "https://api.covid19india.org/csv/latest/state_wise.csv")
            state_wise = pd.read_csv("state_wise.csv")
            self.progressBar.setValue(10)

            # case_time_series = pd.read_csv(
                # "https://api.covid19india.org/csv/latest/case_time_series.csv")
            case_time_series = pd.read_csv("case_time_series.csv")
            self.progressBar.setValue(20)

            # tested_number_icmr_data = pd.read_csv(
                # "https://api.covid19india.org/csv/latest/tested_numbers_icmr_data.csv")
            tested_number_icmr_data = pd.read_csv("tested_numbers_icmr_data.csv")
            self.progressBar.setValue(30)

            # state_wise_daily = pd.read_csv(
                # 'https://api.covid19india.org/csv/latest/state_wise_daily.csv')
            state_wise_daily = pd.read_csv("state_wise_daily.csv")
            self.progressBar.setValue(40)

            vaccine_state = pd.read_csv("vaccine_doses_statewise_v2.csv")
            self.progressBar.setValue(50)

            # statewise_tested_number_data = pd.read_csv(
                # 'https://api.covid19india.org/csv/latest/statewise_tested_numbers_data.csv',low_memory=False)
            statewise_tested_number_data = pd.read_csv("statewise_tested_numbers_data.csv", low_memory=False)
            self.progressBar.setValue(60)

            # vaccine_state_wise = pd.read_csv(
                # 'http://data.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv')
            vaccine_state_wise = pd.read_csv("cowin_vaccine_data_statewise.csv")
            self.progressBar.setValue(70)
            # district_wise = pd.read_csv(
                # 'https://api.covid19india.org/csv/latest/district_wise.csv')
            district_wise = pd.read_csv("district_wise.csv")
            self.progressBar.setValue(80)

            india_vaccine = pd.read_csv("india_vaccine.csv")
            self.progressBar.setValue(90)            

            # districts = pd.read_csv('https://api.covid19india.org/csv/latest/districts.csv')
            districts = pd.read_csv("districts.csv")
            self.progressBar.setValue(100)
            self.progressBar.setFormat('Completed')

        except:
            application = QtWidgets.QApplication(sys.argv)
            QMessageBox.information(None, 'Error', 'No Network Connection',
                                    QMessageBox.Ok,
                                    QMessageBox.Ok)
            sys.exit(0)
        
        ######################## Enabling the buttons ##################
        self.Button_IndiaCurrent.setEnabled(True)
        self.Button_IndiaDaily.setEnabled(True)
        self.Button_IndiaPositivity.setEnabled(True)
        self.Button_IndiaVaccine.setEnabled(True)
        self.Button_VaccineDaily.setEnabled(True)
        self.Button_StateCurrent.setEnabled(True)
        self.Button_StateDaily.setEnabled(True)
        self.Button_StatePositivity.setEnabled(True)
        self.Button_State_vaccine.setEnabled(True)
        self.Button_State_vaccine_daily.setEnabled(True)
        self.Button_State_vaccination_compare.setEnabled(True)
        self.Button_Compare.setEnabled(True)
        self.Button_DistrictStatus.setEnabled(True)
        self.Button_DistrictDaily.setEnabled(True)

        ########################## Assigning values to combobox ###########
        data = state_wise.copy()
        state_names = list(data.State.iloc[1:,].unique())


        data = district_wise.copy()
        district_name = list(data.District.iloc[1:,].unique())


        del_list = ['Other State','Other Region','Unknown']
        district_name = [i for i in district_name if i not in del_list]
        for i in range(0, len(state_names)):
            self.comboBox_State.insertItem(i, _translate(
                "Covid_Analysis", state_names[i], None))
            self.comboBox_State_vaccine.insertItem(i, _translate(
                "Covid_Analysis", state_names[i], None))
            self.comboBox_Compare_1.insertItem(
                i, _translate("Covid_Analysis", state_names[i], None))
            self.comboBox_Compare_2.insertItem(
                i, _translate("Covid_Analysis", state_names[i], None))
            self.comboBox_Compare_3.insertItem(
                i, _translate("Covid_Analysis", state_names[i], None))
        for i in range(0, len(district_name)):
            self.comboBox_District.insertItem(i, _translate(
                "Covid_Analysis", district_name[i], None))
        self.comboBox_State.setCurrentIndex(state_names.index('Rajasthan'))
        self.comboBox_State_vaccine.setCurrentIndex(state_names.index('Rajasthan'))
        self.comboBox_Compare_1.setCurrentIndex(state_names.index('Rajasthan'))
        self.comboBox_Compare_2.setCurrentIndex(state_names.index('Maharashtra'))
        self.comboBox_Compare_3.setCurrentIndex(state_names.index('Gujarat'))
        self.comboBox_District.setCurrentIndex(district_name.index('Udaipur'))


    def India_Current_Status(self):
        india_Current_Status(state_wise)

    def India_Daily_Status(self):
        india_Daily_Status(case_time_series)

    def India_Test_Positivity(self):
        india_Test_Positivity(tested_number_icmr_data,case_time_series)

    def Vaccination_total(self):
        vaccination_total(vaccine_state_wise)
    
    def Vaccination_daily(self):
        vaccination_daily(india_vaccine)
        
    def State_Current_Status(self):
        state = self.comboBox_State.currentText()
        state_Current_Status(state,state_wise)

    def State_Daily_Status(self):
        try:
            state = self.comboBox_State.currentText()
            state_Daily_Status(state,state_wise,state_wise_daily)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")

    def State_Test_Positivity(self):
        try:
           state = self.comboBox_State.currentText()
           state_Test_Positivity(state,statewise_tested_number_data,state_wise,state_wise_daily)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")
    
    def State_vaccine(self):
        # try:
        state = self.comboBox_State_vaccine.currentText()
        state_vaccine(state,vaccine_state_wise)
        # except:
            # error = QtWidgets.QMessageBox.critical(
                # self, 'Error', "Data insufficient for the selected state")
    

    def State_vaccine_daily(self):
        try:    
            state = self.comboBox_State_vaccine.currentText()
            state_vaccine_daily(state)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected state")

    def State_vaccination_compare(self):
        try:
            state1 = self.comboBox_Compare_1.currentText()
            state2 = self.comboBox_Compare_2.currentText()
            state3 = self.comboBox_Compare_3.currentText()
        
            state_vaccination_compare(state1, state2, state3)
        except:
            error = QtWidgets.QMessageBox.critical(self, 'Error', "Data insufficient for the any 1 or more selected state")

    def State_Comparision(self):
        try:
            state_1 = self.comboBox_Compare_1.currentText()
            state_2 = self.comboBox_Compare_2.currentText()
            state_3 = self.comboBox_Compare_3.currentText()
            state_Compare(state_1,state_2,state_3,state_wise,state_wise_daily,statewise_tested_number_data)
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the any 1 or more selected state")

    def District_Current_Status(self):
        district = self.comboBox_District.currentText()
        district_Current_Status(district,district_wise)
    
    def District_Daily_Status(self):
        try:
            district = self.comboBox_District.currentText()
            district_Daily_Status(district,districts)
            
        except:
            error = QtWidgets.QMessageBox.critical(
                self, 'Error', "Data insufficient for the selected district")

            
    def retranslateUi(self, Covid_Analysis):
        Covid_Analysis.setWindowTitle(_translate("Covid_Analysis", "Covid-19 Analysis", None))
        self.label_India.setText(_translate(
            "Covid_Analysis", "India Analysis", None))
        self.label_State.setText(_translate(
            "Covid_Analysis", "State Analysis", None))
        self.label_State_comparison.setText(_translate(
            "Covid_Analysis", "State Comparison", None))
        self.label_District.setText(_translate(
            "Covid_Analysis", "District Analysis", None))
        self.Button_IndiaCurrent.setText(_translate("Covid_Analysis", "Current Status", None))
        self.Button_IndiaDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Status", None))
        self.Button_IndiaPositivity.setText(_translate(
            "Covid_Analysis", "15 Days Daily Test Positivity", None))
        self.Button_IndiaVaccine.setText(_translate(
            "Covid_Analysis", "Current Vaccination", None))
        self.Button_VaccineDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Vaccination", None))
        self.Button_StateCurrent.setText(_translate("Covid_Analysis", "Current Status", None))
        self.Button_StateDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Status", None))
        self.Button_StatePositivity.setText(_translate(
            "Covid_Analysis", "15 Days Daily Test Positivity", None))
        self.Button_State_vaccine.setText(_translate(
            "Covid_Analysis", "Current Vaccination", None))
        self.Button_State_vaccine_daily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Vaccination", None))
        self.Button_State_vaccination_compare.setText(_translate(
            "Covid_Analysis", "Vaccination Compare", None))
        self.Button_Compare.setText(_translate(
            "Covid_Analysis", "Covid-19 Compare", None))
        self.Button_DistrictStatus.setText(_translate(
            "Covid_Analysis", "Current Status", None))
        self.Button_DistrictDaily.setText(_translate(
            "Covid_Analysis", "15 Days Daily Status", None))
        self.Button_GetData.setText(_translate(
            "Covid_Analysis", "Get Data", None))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Covid_Analysis = QtWidgets.QDialog()
    ui = Ui_Covid_Analysis()
    ui.setupUi(Covid_Analysis)
    Covid_Analysis.show()
    sys.exit(app.exec_())


