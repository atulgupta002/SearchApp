# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchApp.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
import webbrowser as wb


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(393, 297)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchText = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchText.setGeometry(QtCore.QRect(20, 80, 351, 41))
        self.SearchText.setObjectName("SearchText")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(11, 11, 351, 41))
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 140, 351, 100))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_GoogleScholar = QtWidgets.QPushButton(self.widget)
        self.pushButton_GoogleScholar.setObjectName("pushButton_GoogleScholar")
        self.pushButton_GoogleScholar.clicked.connect(self.GoogleScholar) #attaching method to button click
        self.gridLayout.addWidget(self.pushButton_GoogleScholar, 0, 0, 1, 1)
        self.pushButton_YouTube = QtWidgets.QPushButton(self.widget)
        self.pushButton_YouTube.setObjectName("pushButton_YouTube")
        self.pushButton_YouTube.clicked.connect(self.YouTube) #attaching method to button click
        self.gridLayout.addWidget(self.pushButton_YouTube, 1, 1, 1, 1)
        self.pushButton_GoogleMaps = QtWidgets.QPushButton(self.widget)
        self.pushButton_GoogleMaps.setObjectName("pushButton_GoogleMaps")
        self.pushButton_GoogleMaps.clicked.connect(self.GoogleMaps) #attaching method to button click
        self.gridLayout.addWidget(self.pushButton_GoogleMaps, 1, 2, 1, 1)
        self.pushButton_Amazon = QtWidgets.QPushButton(self.widget)
        self.pushButton_Amazon.setObjectName("pushButton_Amazon")
        self.pushButton_Amazon.clicked.connect(self.Amazon) #attaching method to button click
        self.gridLayout.addWidget(self.pushButton_Amazon, 1, 0, 1, 1)
        self.pushButton_Google = QtWidgets.QPushButton(self.widget)
        self.pushButton_Google.setObjectName("pushButton_Google")
        self.pushButton_Google.clicked.connect(self.Google) #attaching method to button click
        self.gridLayout.addWidget(self.pushButton_Google, 0, 1, 1, 1)
        self.pushButton_Wikipedia = QtWidgets.QPushButton(self.widget)
        self.pushButton_Wikipedia.setObjectName("pushButton_Wikipedia")
        self.gridLayout.addWidget(self.pushButton_Wikipedia, 0, 2, 1, 1)
        self.pushButton_Wikipedia.clicked.connect(self.Wikipedia) #attaching method to button click
        self.pushButton_IMDb = QtWidgets.QPushButton(self.widget)
        self.pushButton_IMDb.setObjectName("pushButton_IMDb")
        self.gridLayout.addWidget(self.pushButton_IMDb, 2, 1, 1, 1)
        self.pushButton_IMDb.clicked.connect(self.IMDb) #attaching method to button click
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 393, 26))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuMenu.addAction(self.actionAbout)
        self.menuMenu.addAction(self.actionExit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Search app"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">Search</span></p></body></html>"))
        self.pushButton_GoogleScholar.setText(_translate("MainWindow", "Google Scholar"))
        self.pushButton_YouTube.setText(_translate("MainWindow", "YouTube"))
        self.pushButton_GoogleMaps.setText(_translate("MainWindow", "Google Maps"))
        self.pushButton_Amazon.setText(_translate("MainWindow", "Amazon"))
        self.pushButton_Google.setText(_translate("MainWindow", "Google"))
        self.pushButton_Wikipedia.setText(_translate("MainWindow", "Wikipedia"))
        self.pushButton_IMDb.setText(_translate("MainWindow", "IMDb"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

    def Google(self):
        self.inputString = self.SearchText.text()
        query = 'https://www.google.com/search?q=' + self.inputString
        wb.open(query)

    def GoogleScholar(self):
        self.inputString = self.SearchText.text()
        query = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='+ self.inputString
        wb.open(query)

    def YouTube(self):
        self.inputString = self.SearchText.text()
        query = 'https://www.youtube.com/results?search_query=' + self.inputString
        wb.open(query)

    def GoogleMaps(self):
        self.inputString = self.SearchText.text()
        query = 'https://www.google.com/maps/place/' + self.inputString
        wb.open(query)

    def IMDb(self):
        self.inputString = self.SearchText.text()
        query = 'https://www.imdb.com/find?q=' + self.inputString + '+&ref_=nv_sr_sm'
        wb.open(query)

    def Amazon(self):
        self.inputString = self.SearchText.text()
        query = 'https://www.amazon.com/s?k=' + self.inputString + '&ref=nb_sb_noss_2'
        wb.open(query)

    def Wikipedia(self):
        self.inputString = self.SearchText.text()
        query = 'https://en.wikipedia.org/wiki/' + self.inputString
        wb.open(query)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
