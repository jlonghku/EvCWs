# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jlong/EvCWs/ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1219, 718)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 40, 1243, 658))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_3 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.groupBox_3)
        self.label_14.setObjectName("label_14")
        self.gridLayout_3.addWidget(self.label_14, 4, 10, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 4, 0, 1, 3)
        self.checkBox_10 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_10.setObjectName("checkBox_10")
        self.gridLayout_3.addWidget(self.checkBox_10, 4, 17, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.groupBox_3)
        self.label_17.setObjectName("label_17")
        self.gridLayout_3.addWidget(self.label_17, 5, 3, 1, 2)
        self.spinBox_14 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_14.setMaximum(1)
        self.spinBox_14.setObjectName("spinBox_14")
        self.gridLayout_3.addWidget(self.spinBox_14, 3, 16, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.spinBox_25 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_25.setMaximum(2)
        self.spinBox_25.setObjectName("spinBox_25")
        self.gridLayout_3.addWidget(self.spinBox_25, 5, 5, 1, 2)
        self.spinBox_22 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_22.setMaximum(2)
        self.spinBox_22.setObjectName("spinBox_22")
        self.gridLayout_3.addWidget(self.spinBox_22, 4, 8, 1, 2)
        self.spinBox_26 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_26.setMaximum(2)
        self.spinBox_26.setObjectName("spinBox_26")
        self.gridLayout_3.addWidget(self.spinBox_26, 5, 10, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox_3)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 3, 12, 1, 2)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_3, 1, 9, 1, 5)
        self.spinBox_13 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_13.setMaximum(1)
        self.spinBox_13.setObjectName("spinBox_13")
        self.gridLayout_3.addWidget(self.spinBox_13, 3, 14, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.groupBox_3)
        self.label_16.setObjectName("label_16")
        self.gridLayout_3.addWidget(self.label_16, 4, 14, 1, 2)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_2, 1, 1, 1, 4)
        self.spinBox_21 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_21.setMaximum(2)
        self.spinBox_21.setObjectName("spinBox_21")
        self.gridLayout_3.addWidget(self.spinBox_21, 4, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 7, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.groupBox_3)
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName("label_18")
        self.gridLayout_3.addWidget(self.label_18, 3, 0, 1, 2)
        self.checkBox_1 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_1.setCheckable(True)
        self.checkBox_1.setChecked(False)
        self.checkBox_1.setTristate(False)
        self.checkBox_1.setObjectName("checkBox_1")
        self.gridLayout_3.addWidget(self.checkBox_1, 2, 6, 1, 4)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 0, 10, 1, 2)
        self.spinBox_12 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_12.setMaximum(1)
        self.spinBox_12.setObjectName("spinBox_12")
        self.gridLayout_3.addWidget(self.spinBox_12, 3, 11, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.groupBox_3)
        self.label_15.setObjectName("label_15")
        self.gridLayout_3.addWidget(self.label_15, 5, 8, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.groupBox_3)
        self.label_22.setObjectName("label_22")
        self.gridLayout_3.addWidget(self.label_22, 3, 15, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.gridLayout_3.addWidget(self.label_2, 2, 0, 1, 3)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout_3.addWidget(self.checkBox_3, 2, 13, 1, 4)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_3.addWidget(self.checkBox_2, 2, 10, 1, 3)
        self.spinBox_11 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_11.setMaximum(1)
        self.spinBox_11.setObjectName("spinBox_11")
        self.gridLayout_3.addWidget(self.spinBox_11, 3, 7, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 4, 3, 1, 1)
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.gridLayout_3.addWidget(self.comboBox_1, 0, 1, 1, 9)
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_3)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_3.addWidget(self.checkBox, 2, 3, 1, 3)
        self.label_20 = QtWidgets.QLabel(self.groupBox_3)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 3, 2, 1, 5)
        self.spinBox_23 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_23.setMaximum(2)
        self.spinBox_23.setObjectName("spinBox_23")
        self.gridLayout_3.addWidget(self.spinBox_23, 4, 12, 1, 1)
        self.spinBox_24 = QtWidgets.QSpinBox(self.groupBox_3)
        self.spinBox_24.setMaximum(2)
        self.spinBox_24.setObjectName("spinBox_24")
        self.gridLayout_3.addWidget(self.spinBox_24, 4, 16, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox_3)
        self.label_13.setObjectName("label_13")
        self.gridLayout_3.addWidget(self.label_13, 4, 7, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox_3)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 3, 8, 1, 3)
        self.verticalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout.addWidget(self.comboBox_4)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_27 = QtWidgets.QLabel(self.groupBox)
        self.label_27.setObjectName("label_27")
        self.gridLayout_2.addWidget(self.label_27, 0, 0, 1, 1)
        self.label11 = QtWidgets.QLabel(self.groupBox)
        self.label11.setObjectName("label11")
        self.gridLayout_2.addWidget(self.label11, 0, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setObjectName("label_24")
        self.gridLayout_2.addWidget(self.label_24, 0, 2, 1, 1)
        self.label12 = QtWidgets.QLabel(self.groupBox)
        self.label12.setObjectName("label12")
        self.gridLayout_2.addWidget(self.label12, 0, 3, 1, 1)
        self.label_26 = QtWidgets.QLabel(self.groupBox)
        self.label_26.setObjectName("label_26")
        self.gridLayout_2.addWidget(self.label_26, 1, 0, 1, 1)
        self.label13 = QtWidgets.QLabel(self.groupBox)
        self.label13.setObjectName("label13")
        self.gridLayout_2.addWidget(self.label13, 1, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setObjectName("label_25")
        self.gridLayout_2.addWidget(self.label_25, 1, 2, 1, 1)
        self.label14 = QtWidgets.QLabel(self.groupBox)
        self.label14.setObjectName("label14")
        self.gridLayout_2.addWidget(self.label14, 1, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.widget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName("gridLayout")
        self.label_34 = QtWidgets.QLabel(self.groupBox_2)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 1)
        self.label21 = QtWidgets.QLabel(self.groupBox_2)
        self.label21.setObjectName("label21")
        self.gridLayout.addWidget(self.label21, 0, 1, 1, 1)
        self.label_37 = QtWidgets.QLabel(self.groupBox_2)
        self.label_37.setObjectName("label_37")
        self.gridLayout.addWidget(self.label_37, 0, 2, 1, 1)
        self.label22 = QtWidgets.QLabel(self.groupBox_2)
        self.label22.setObjectName("label22")
        self.gridLayout.addWidget(self.label22, 0, 3, 1, 1)
        self.label_38 = QtWidgets.QLabel(self.groupBox_2)
        self.label_38.setObjectName("label_38")
        self.gridLayout.addWidget(self.label_38, 1, 0, 1, 1)
        self.label23 = QtWidgets.QLabel(self.groupBox_2)
        self.label23.setObjectName("label23")
        self.gridLayout.addWidget(self.label23, 1, 1, 1, 1)
        self.label_36 = QtWidgets.QLabel(self.groupBox_2)
        self.label_36.setObjectName("label_36")
        self.gridLayout.addWidget(self.label_36, 1, 2, 1, 1)
        self.label24 = QtWidgets.QLabel(self.groupBox_2)
        self.label24.setObjectName("label24")
        self.gridLayout.addWidget(self.label24, 1, 3, 1, 1)
        self.label_39 = QtWidgets.QLabel(self.groupBox_2)
        self.label_39.setObjectName("label_39")
        self.gridLayout.addWidget(self.label_39, 2, 0, 1, 1)
        self.label25 = QtWidgets.QLabel(self.groupBox_2)
        self.label25.setObjectName("label25")
        self.gridLayout.addWidget(self.label25, 2, 1, 1, 1)
        self.label_35 = QtWidgets.QLabel(self.groupBox_2)
        self.label_35.setObjectName("label_35")
        self.gridLayout.addWidget(self.label_35, 2, 2, 1, 1)
        self.label26 = QtWidgets.QLabel(self.groupBox_2)
        self.label26.setObjectName("label26")
        self.gridLayout.addWidget(self.label26, 2, 3, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Basic features of constructed wetlands"))
        self.label.setText(_translate("MainWindow", "Scale:"))
        self.label_14.setText(_translate("MainWindow", "Nitrogen"))
        self.label_5.setText(_translate("MainWindow", "Water quality:"))
        self.checkBox_10.setText(_translate("MainWindow", "PPCPs"))
        self.label_17.setText(_translate("MainWindow", "Pesticides"))
        self.label_3.setText(_translate("MainWindow", "Type:"))
        self.label_21.setText(_translate("MainWindow", "Water level"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1.Free water surface flow"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "2.Horizontal subsurface flow"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "3.Vertical subsurface flow"))
        self.label_16.setText(_translate("MainWindow", "Phosphorus"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "1.Laboratory"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "2.Small"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "3.Large"))
        self.label_11.setText(_translate("MainWindow", "Flow type"))
        self.label_18.setText(_translate("MainWindow", "Hydraulic conditions"))
        self.checkBox_1.setText(_translate("MainWindow", "Domestic sewer system"))
        self.pushButton_2.setText(_translate("MainWindow", "Apply"))
        self.label_15.setText(_translate("MainWindow", "Heavy metals"))
        self.label_22.setText(_translate("MainWindow", "HRT"))
        self.label_2.setText(_translate("MainWindow", "Inflow sources:"))
        self.checkBox_3.setText(_translate("MainWindow", "Other natural water bodies"))
        self.checkBox_2.setText(_translate("MainWindow", "Industary drainage"))
        self.label_12.setText(_translate("MainWindow", "DO"))
        self.comboBox_1.setItemText(0, _translate("MainWindow", "1.Stormwater management"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "2.Municipal wastewater treatment"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "3.Industrial wastewater treatment"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "4.Agricultural pollutants removal"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "5.Purification of natural water bodies"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "6.Mine drainage treatment"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "7.Ecosystem restoration"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "8.User-defined"))
        self.checkBox.setText(_translate("MainWindow", "Rainfall"))
        self.label_20.setText(_translate("MainWindow", "Inflow loading rate"))
        self.label_13.setText(_translate("MainWindow", "BOD"))
        self.label_23.setText(_translate("MainWindow", "Flow fluctuation"))
        self.label_4.setText(_translate("MainWindow", "Changing hydrological conditions"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "1.Wet seasons"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "2.Dry seasons"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "3.Prolonged flooding"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "4.Rainstrom"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "5.Highly fluctuating flow"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "6.Short-term inundation"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "7.Circular-flow corridor and baffled subsurface flow CWs"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "8.Tidal-operated CWs"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "9.Clogging of porous media"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "10.Artificial pulsing in subsurface CWs"))
        self.pushButton.setText(_translate("MainWindow", "Evaluate"))
        self.groupBox.setTitle(_translate("MainWindow", "Possible change in hydraulic conditions"))
        self.label_27.setText(_translate("MainWindow", "Inflow loading rate"))
        self.label11.setText(_translate("MainWindow", "-"))
        self.label_24.setText(_translate("MainWindow", "Flow fluctuation"))
        self.label12.setText(_translate("MainWindow", "-"))
        self.label_26.setText(_translate("MainWindow", "Water level"))
        self.label13.setText(_translate("MainWindow", "-"))
        self.label_25.setText(_translate("MainWindow", "HRT"))
        self.label14.setText(_translate("MainWindow", "-"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Possible change in water quality"))
        self.label_34.setText(_translate("MainWindow", "DO"))
        self.label21.setText(_translate("MainWindow", "-"))
        self.label_37.setText(_translate("MainWindow", "BOD"))
        self.label22.setText(_translate("MainWindow", "-"))
        self.label_38.setText(_translate("MainWindow", "Nitrogen"))
        self.label23.setText(_translate("MainWindow", "-"))
        self.label_36.setText(_translate("MainWindow", "Phosphorus"))
        self.label24.setText(_translate("MainWindow", "-"))
        self.label_39.setText(_translate("MainWindow", "Pesticides"))
        self.label25.setText(_translate("MainWindow", "-"))
        self.label_35.setText(_translate("MainWindow", "Heavy metals"))
        self.label26.setText(_translate("MainWindow", "-"))

