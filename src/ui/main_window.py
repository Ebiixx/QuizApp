from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ComboBox for topic selection
        self.topicComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.topicComboBox.setGeometry(QtCore.QRect(50, 50, 300, 30))
        self.topicComboBox.setObjectName("topicComboBox")

        # Start button
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(50, 100, 100, 30))
        self.startButton.setObjectName("startButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quiz App"))
        self.startButton.setText(_translate("MainWindow", "Start Quiz"))