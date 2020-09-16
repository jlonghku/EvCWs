import sys
import numpy
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_ui import Ui_MainWindow
from PyQt5 import QtCore
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

class MyMainWindow(QMainWindow,Ui_MainWindow):
  def __init__(self,parent = None):
    super(MyMainWindow, self).__init__(parent)
    self.setupUi(self)
    self.pushButton.clicked.connect(self.cal)
    self.pushButton_2.clicked.connect(self.tem)

# set template of different constructed wetlands
  def tem(self):
    cb0=[self.comboBox_1.currentIndex(),self.comboBox_2.currentIndex(),self.comboBox_3.currentIndex(),self.comboBox_4.currentIndex()]
    if cb0[0]==0:
      setcb0(self,[1,0])
      setcb(self,[1,0,0,0])
      setsp(self,[1,1,1,1],[1,1,1,0,0,0]) 
    elif cb0[0]==1:
      setcb0(self,[0,1])
      setcb(self,[0,1,0,0])
      setsp(self,[1,1,1,1],[1,1,1,0,1,0])
    elif cb0[0]==2:
      setcb0(self,[0,1])
      setcb(self,[0,1,0,0])
      setsp(self,[1,1,1,1],[0,0,1,0,0,1])
    elif cb0[0]==3:
      setcb0(self,[1,0])
      setcb(self,[1,0,0,1])
      setsp(self,[1,1,1,1],[1,1,0,0,1,0])
    elif cb0[0]==4:
      setcb0(self,[2,1])
      setcb(self,[1,0,0,1])
      setsp(self,[1,1,1,1],[1,1,1,1,0,0])
    elif cb0[0]==5:
      setcb0(self,[1,1])
      setcb(self,[1,0,0,1])
      setsp(self,[1,1,1,1],[0,0,1,0,0,1])
    elif cb0[0]==56:
      setcb0(self,[2,1])
      setcb(self,[1,0,0,1])
      setsp(self,[1,1,1,1],[1,1,0,1,0,0])
    elif cb0[0]==7:
      setcb0(self,[0,0])
      setcb(self,[0,0,0,0])
      setsp(self,[1,1,1,1],[0,0,0,0,0,0])

  def cal(self):
    cb0=[self.comboBox_1.currentIndex(),self.comboBox_2.currentIndex(),self.comboBox_3.currentIndex(),self.comboBox_4.currentIndex()]
    cb=[self.checkBox.isChecked(),self.checkBox_1.isChecked(),self.checkBox_2.isChecked(),self.checkBox_3.isChecked()]
    sp1=[self.spinBox_11.value(),self.spinBox_12.value(),self.spinBox_13.value(),self.spinBox_14.value()]
    sp2=[self.spinBox_21.value(),self.spinBox_22.value(),self.spinBox_23.value(),self.spinBox_24.value(),self.spinBox_25.value(),self.spinBox_26.value()]
    T=[[2,0,1,-1],[-2,0,-1,1],[1,0,2,1],[2,1,1,-1],[0,2,0,0],[0,0,2,1],[0,0,0,2],[0,2,0,0],[0,0,0,-2],[0,2,0,0]]
    SP1=numpy.array(T[cb0[3]])+numpy.array(sp1)
    if cb0[1]==0 :
      SP1=SP1+numpy.sign(SP1)
    if cb0[2]!=0:
      sp1[2]=0
    if ((cb[0]==0&cb[3]==0)&((cb0[3]==0)|(cb0[3]==1)|(cb0[3]==2)|(cb0[3]==3))):
      SP1=[0,0,0,0]
      SP2=[0,0,0,0,0,0]
      setlb1(self,SP1)
      setlb2(self,SP2)
    else:
      SP1=SP1*sp1
      setlb1(self,SP1)
      T2=[[-1,1,1,1,1,1],[1,-1,-1,1,-1,1],[-1,1,1,-1,1,-1],[1,-1,-1,-1,-1,-1]]
      SP2=SP1.dot(numpy.array(T2))
      SP2=SP2*numpy.sign(sp2)
      setlb2(self,SP2)


def setlb2(self,a) :
  self.label21.setText(strrs(a[0]))
  self.label22.setText(strrs(a[1]))
  self.label23.setText(strrs(a[2]))
  self.label24.setText(strrs(a[3]))
  self.label25.setText(strrs(a[4]))
  self.label26.setText(strrs(a[5]))
  

def strrs(a):
  if a==0:
    return "-"
  elif 0<a<=1:
    return "Increase slightly"
  elif 1<a<=2:
    return "Increase"
  elif a>2:
    return "Increase significantly"
  elif -1<=a<0:
    return "Decrease slightly"
  elif-2<=a<-1:
    return "Decrease "
  elif a<=-2:
    return "Decrease significantly"


  

def setlb1(self,a):
  self.label11.setText(strrs(a[0]))
  self.label12.setText(strrs(a[1]))
  self.label13.setText(strrs(a[2]))
  self.label14.setText(strrs(a[3]))

def setcb(self,a):
  self.checkBox.setChecked(a[0])
  self.checkBox_1.setChecked(a[1])
  self.checkBox_2.setChecked(a[2])
  self.checkBox_3.setChecked(a[3])

def setcb0(self,a):
  self.comboBox_2.setCurrentIndex(a[0])
  self.comboBox_3.setCurrentIndex(a[1])


def setsp(self,a,b):
  self.spinBox_11.setValue(a[0])
  self.spinBox_12.setValue(a[1])
  self.spinBox_13.setValue(a[2])
  self.spinBox_14.setValue(a[3])
  self.spinBox_21.setValue(b[0])
  self.spinBox_22.setValue(b[1])
  self.spinBox_23.setValue(b[2])
  self.spinBox_24.setValue(b[3])
  self.spinBox_25.setValue(b[4])
  self.spinBox_26.setValue(b[5])


   
    
if __name__ =="__main__":
  
  app = QApplication(sys.argv)
  myWin = MyMainWindow()
  #myWin.setFixedSize(1200,800) 
  myWin.show()
  
  sys.exit(app.exec_())