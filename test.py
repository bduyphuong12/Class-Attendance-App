import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("QMainWindow{""border-image:url(back_ground.jpg);""background-color:rgb(0,255,255);""\n""}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 751, 501))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 511, 421))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setMouseTracking(True)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 50, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(270, 50, 121, 21))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(130, 50, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.setCurrentText("AI")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(400, 50, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(40, 460, 131, 31))
        self.pushButton.setStyleSheet("color: rgb(255, 89, 97);\n""background-color: rgb(252, 238, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 460, 111, 31))
        self.pushButton_2.setStyleSheet("color: rgb(255, 89, 97);\n""background-color: rgb(252, 238, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(590, 410, 141, 31))
        self.pushButton_3.setStyleSheet("color: rgb(255, 89, 97);\n""background-color: rgb(252, 238, 255);")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(590, 460, 141, 31))
        self.pushButton_4.setStyleSheet("color: rgb(255, 89, 97);\n""background-color: rgb(252, 238, 255);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(580, 70, 161, 231))
        self.groupBox_2.setAutoFillBackground(True)
        self.groupBox_2.setObjectName("groupBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #event
        self.pushButton.clicked.connect(self.btnExitClick)

        
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Màn hình nhận diện"))
        self.label.setText(_translate("MainWindow", "Chọn môn học"))
        self.label_2.setText(_translate("MainWindow", "Chọn loại điểm danh"))
        self.pushButton.setText(_translate("MainWindow", "Điểm danh"))
        self.pushButton_2.setText(_translate("MainWindow", "Kết thúc"))
        self.pushButton_3.setText(_translate("MainWindow", "SV chưa điểm danh"))
        self.pushButton_4.setText(_translate("MainWindow", "Điểm danh thủ công"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Thông tin sinh viên"))
        textLoaiDiemDanh = "điểm danh tự động"
        textMonHoc = "AI"
        self.comboBox.addItem(textMonHoc)
        self.comboBox_2.addItem(textLoaiDiemDanh)

    def btnExitClick(self):
        print("press")

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Chào")
        msg.setInformativeText(" Tổng chi phí là vnđ")
        msg.setWindowTitle("Chi phí")
        msg.exec_()

if __name__ == "__main__":
    # app = QtWidgets.QApplication(sys.argv)
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    # MainWindow.show()
    # sys.exit(app.exec_())

    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
