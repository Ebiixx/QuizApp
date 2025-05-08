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

        # Question label
        self.questionLabel = QtWidgets.QLabel(self.centralwidget)
        self.questionLabel.setGeometry(QtCore.QRect(50, 150, 700, 50))
        self.questionLabel.setWordWrap(True)
        self.questionLabel.setObjectName("questionLabel")

        # Radio buttons for answers
        self.answer1 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer1.setGeometry(QtCore.QRect(50, 220, 700, 30))
        self.answer1.setObjectName("answer1")

        self.answer2 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer2.setGeometry(QtCore.QRect(50, 260, 700, 30))
        self.answer2.setObjectName("answer2")

        self.answer3 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer3.setGeometry(QtCore.QRect(50, 300, 700, 30))
        self.answer3.setObjectName("answer3")

        self.answer4 = QtWidgets.QRadioButton(self.centralwidget)
        self.answer4.setGeometry(QtCore.QRect(50, 340, 700, 30))
        self.answer4.setObjectName("answer4")

        # Submit button
        self.submitButton = QtWidgets.QPushButton(self.centralwidget)
        self.submitButton.setGeometry(QtCore.QRect(50, 400, 100, 30))
        self.submitButton.setObjectName("submitButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quiz App"))
        self.startButton.setText(_translate("MainWindow", "Start Quiz"))
        self.submitButton.setText(_translate("MainWindow", "Submit"))