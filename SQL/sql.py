from designers import Ui_MainWindow
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon,QPixmap
from PyQt5.QtWidgets import QInputDialog,QLineEdit,QMessageBox,QLabel
import sys
import mysql.connector

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(":/icons/lgo.png"))
        self.setWindowTitle("Öğrenci bilgi sistemi")

        self.setStyleSheet("#MainWindow{border-image: url(:/icons/yazilim.png)};")


        label=QLabel(self)
        label.setPixmap(QPixmap(":/icons/py.png"))
        label.move(747,15)
        label.resize(400,300)

        self.ui.lbl_sql.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.lbl_data.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.lbl_ulke.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.radio_tr.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.radio_england.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.radio_arabic.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.radio_russia.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.radio_germany.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.lbl_ulke_2.setStyleSheet("font: 75 10pt 'MS Shell Dlg 2';border-radius:10px;color:rgb(170, 255, 255);")
        self.ui.lbl_ulke_3.setStyleSheet("font: 12pt 'MV Boli';border-radius:10px;color:rgb(170, 255, 255);")





        self.ui.btn_ekle.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.btn_guncelle.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.btn_yukari.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.btn_asagi.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.btn_sil.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.btn_exit.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 0, 0);font: 75 12pt 'MS Shell Dlg 2';color: rgb(176, 249, 255);")
        self.ui.btn_veriCek.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.pushButton_7.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")
        self.ui.btn_sirala.setStyleSheet("border-radius:8px;background-color:qlineargradient(spread:pad, x1:0.165, y1:0.840909, x2:1, y2:0, stop:0 rgba(0, 43, 107, 255), stop:1 rgba(255, 255, 255, 255));color:rgb(255, 170, 0);font: 75 10pt 'MS Shell Dlg 2';color: rgb(210, 252, 255);")

        self.item()

        self.ui.btn_ekle.clicked.connect(self.ekle)
        self.ui.btn_sil.clicked.connect(self.sil)
        self.ui.pushButton_7.clicked.connect(self.veriGonder)
        self.ui.btn_veriCek.clicked.connect(self.vericek)
        self.ui.btn_guncelle.clicked.connect(self.guncelle)
        self.ui.btn_yukari.clicked.connect(self.yukari)
        self.ui.btn_asagi.clicked.connect(self.asagi)
        self.ui.btn_exit.clicked.connect(self.exit)
        self.ui.btn_sirala.clicked.connect(self.sirala)


    def item(self):
        self.ui.listWidget_data.addItems(["Mert", "Ali", "Osman"])

    def ekle(self):
        index=self.ui.listWidget_data.currentRow()
        if index is not None:
            text,ok=QInputDialog.getText(self,"Veri ekle","İsim giriniz")
            if text and ok is not None:
                self.ui.listWidget_data.insertItem(index,text)
            else:
                return

    def guncelle(self):
        index=self.ui.listWidget_data.currentRow()
        item=self.ui.listWidget_data.takeItem(index)

        if index and item is None:
            QMessageBox.question(self,"Error","Veri bulunamadı",QMessageBox.Ok)
        else:
            text, ok = QInputDialog.getText(self, "Veri güncelle", "Yeni isim giriniz", QLineEdit.Normal, item.text())
            if ok== False:
                self.ui.listWidget_data.insertItem(index,item.text())
            else:
                self.ui.listWidget_data.insertItem(index,text)

    def yukari(self):
        index = self.ui.listWidget_data.currentRow()
        if index>=1:
            item = self.ui.listWidget_data.takeItem(index)
            self.ui.listWidget_data.insertItem(index - 1, item)
            self.ui.listWidget_data.setCurrentItem(item)
        else:
            return

    def asagi(self):
        index=self.ui.listWidget_data.currentRow()
        if index < self.ui.listWidget_data.count()-1:
            item = self.ui.listWidget_data.takeItem(index)
            self.ui.listWidget_data.insertItem(index+1,item)
            self.ui.listWidget_data.setCurrentItem(item)
        else:
            return

    def sil(self):

        index = self.ui.listWidget_data.currentRow()
        item=self.ui.listWidget_data.takeItem(index)
        if index and item is None:
            QMessageBox.question(self,"Error","Veri seçilmedi",QMessageBox.Ok)
        else:
            ok=QMessageBox.question(self,"Deleted",f"{item.text()} kişisini silmek istediğinizden emin misiniz",QMessageBox.Ok,QMessageBox.Cancel)
            if ok==QMessageBox.Ok:
                del item
            else:
                self.ui.listWidget_data.insertItem(index,item.text())

    def veriGonder(self):
        connect = mysql.connector.connect(
            host="localhost", # Bu alana MySQL serverinizin host alanını giriniz
            user="root",      # Bu alana MySQL serverinizin user alanını giriniz
            password="eyupeser", # Bu alana MySQL serverinizin parolasını giriniz
            database="yenicalismam" # Bu alana MySQL serveriniz içerisinde çalışma yapmak istediğiniz verilerin olduğu alanı giriniz
        )
        cursor = connect.cursor()
        sql = "Select ad,soyad from bilgi" # 'bilgi' yazan yere verilerini görmek istediğiniz alanı giriniz. 'ad' ve 'soyad' yazan yerler yerine istediğiniz kolon isimlerini giriniz
        cursor.execute(sql)
        result1=[i[0].__str__().capitalize() for i in cursor.fetchall()] # Burada girdiğiniz kolonları bölmek istediğiniz şekilde for ile ayarlayınız

        a=len(result1)

        if self.ui.listWidget_sql.count() == a:
            QMessageBox.question(self,"Message","Veriler aktarıldı.",QMessageBox.Ok)
        else:
            self.ui.lbl_sql.setText("SQL veriler")
            self.ui.listWidget_sql.addItems(result1)

    def vericek(self):
        index=self.ui.listWidget_sql.currentRow()

        if index is None:
            QMessageBox.question(self, "Error", "Veri çekmek içi Veri Gör butonunu seçiniz", QMessageBox.Ok)
        else:
            if index is not None:
                item = self.ui.listWidget_sql.takeItem(index)
                self.ui.listWidget_data.insertItem(index,item)
                self.ui.listWidget_sql.insertItem(index,item.text())

    def sirala(self):
        self.ui.listWidget_data.sortItems()

    def exit(self):
        result=QMessageBox.question(self,"Exit","Çıkmak istediğinizden emin misiniz",QMessageBox.Ok|QMessageBox.Cancel)
        if result==QMessageBox.Ok:
            quit()
        else:
            return

def app():
    app = QtWidgets.QApplication(sys.argv)

    win = MyApp()
    win.show()
    sys.exit(app.exec_())
app()


