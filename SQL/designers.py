# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1401, 926)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget_data = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_data.setGeometry(QtCore.QRect(900, 370, 256, 391))
        self.listWidget_data.setObjectName("listWidget_data")
        self.listWidget_sql = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_sql.setGeometry(QtCore.QRect(580, 400, 256, 341))
        self.listWidget_sql.setObjectName("listWidget_sql")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(640, 760, 111, 61))
        self.pushButton_7.setObjectName("pushButton_7")
        self.lbl_data = QtWidgets.QLabel(self.centralwidget)
        self.lbl_data.setGeometry(QtCore.QRect(900, 320, 71, 21))
        self.lbl_data.setObjectName("lbl_data")
        self.lbl_sql = QtWidgets.QLabel(self.centralwidget)
        self.lbl_sql.setGeometry(QtCore.QRect(580, 330, 161, 31))
        self.lbl_sql.setText("")
        self.lbl_sql.setObjectName("lbl_sql")
        self.lbl_ulke_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ulke_2.setGeometry(QtCore.QRect(730, 850, 691, 41))
        self.lbl_ulke_2.setObjectName("lbl_ulke_2")
        self.lbl_ulke_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ulke_3.setGeometry(QtCore.QRect(850, 20, 191, 31))
        self.lbl_ulke_3.setObjectName("lbl_ulke_3")
        self.lbl_ulke = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ulke.setGeometry(QtCore.QRect(370, 350, 71, 21))
        self.lbl_ulke.setObjectName("lbl_ulke")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(370, 390, 111, 211))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_tr = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_tr.setObjectName("radio_tr")
        self.verticalLayout.addWidget(self.radio_tr)
        self.radio_england = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_england.setObjectName("radio_england")
        self.verticalLayout.addWidget(self.radio_england)
        self.radio_germany = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_germany.setObjectName("radio_germany")
        self.verticalLayout.addWidget(self.radio_germany)
        self.radio_arabic = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_arabic.setObjectName("radio_arabic")
        self.verticalLayout.addWidget(self.radio_arabic)
        self.radio_russia = QtWidgets.QRadioButton(self.layoutWidget)
        self.radio_russia.setObjectName("radio_russia")
        self.verticalLayout.addWidget(self.radio_russia)
        self.btn_ekle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ekle.setGeometry(QtCore.QRect(1170, 370, 109, 41))
        self.btn_ekle.setObjectName("btn_ekle")
        self.btn_guncelle = QtWidgets.QPushButton(self.centralwidget)
        self.btn_guncelle.setGeometry(QtCore.QRect(1170, 420, 109, 41))
        self.btn_guncelle.setObjectName("btn_guncelle")
        self.btn_yukari = QtWidgets.QPushButton(self.centralwidget)
        self.btn_yukari.setGeometry(QtCore.QRect(1170, 520, 109, 41))
        self.btn_yukari.setObjectName("btn_yukari")
        self.btn_asagi = QtWidgets.QPushButton(self.centralwidget)
        self.btn_asagi.setGeometry(QtCore.QRect(1170, 570, 109, 41))
        self.btn_asagi.setObjectName("btn_asagi")
        self.btn_sirala = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sirala.setGeometry(QtCore.QRect(1170, 620, 109, 41))
        self.btn_sirala.setObjectName("btn_sirala")
        self.btn_sil = QtWidgets.QPushButton(self.centralwidget)
        self.btn_sil.setGeometry(QtCore.QRect(1170, 670, 109, 41))
        self.btn_sil.setObjectName("btn_sil")
        self.btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_exit.setGeometry(QtCore.QRect(1170, 720, 109, 41))
        self.btn_exit.setObjectName("btn_exit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1401, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_7.setText(_translate("MainWindow", "Veriler (SQL)"))
        self.lbl_data.setText(_translate("MainWindow", "Veriler"))
        self.lbl_ulke_3.setText(_translate("MainWindow", "inst: python3740"))
        self.lbl_ulke.setText(_translate("MainWindow", "Dil"))
        self.radio_tr.setText(_translate("MainWindow", "Türkçe"))
        self.radio_england.setText(_translate("MainWindow", "English"))
        self.radio_germany.setText(_translate("MainWindow", "Deutsch"))
        self.radio_arabic.setText(_translate("MainWindow", "عربي"))
        self.radio_russia.setText(_translate("MainWindow", "Русский"))
        self.btn_ekle.setText(_translate("MainWindow", "ekle"))
        self.btn_guncelle.setText(_translate("MainWindow", "güncelle"))
        self.btn_yukari.setText(_translate("MainWindow", "yukarı"))
        self.btn_asagi.setText(_translate("MainWindow", "aşağı"))
        self.btn_sirala.setText(_translate("MainWindow", "Sırala"))
        self.btn_sil.setText(_translate("MainWindow", "sil"))
        self.btn_exit.setText(_translate("MainWindow", "Çıkış"))
import image_rc
