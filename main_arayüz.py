# -*- coding: utf-8 -*-
from PyQt5 import QtWidgets,QtGui,QtCore
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap,QPainter
import sys,os
import xlwt
import xlsxwriter as ex
import pandas as pd
import sqlite3
import time
class ana_ekran(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.elemanlar()
        self.setGeometry(600,200,500,600)

    def elemanlar(self):
        self.label = QtWidgets.QLabel()
        self.pixmap = QPixmap('paü.png').scaled(100, 100)
        self.label.setPixmap(self.pixmap)
        p=QtWidgets.QVBoxLayout()
        p.addWidget(self.label)
        self.timerlabel = QtWidgets.QLabel("TİMER")
        self.baslik=QtWidgets.QLabel("VERİ MADENCİLİĞİ UYGULAMALARI")
        p.addWidget(self.timerlabel)
        self.l1_baslik = QtWidgets.QLabel(" ")
        self.l2_baslik = QtWidgets.QLabel(" ")
        self.adres_cubugu=QtWidgets.QLineEdit()
        self.adres_cubugu.setStyleSheet("background-color:white")
        self.veri_al=QtWidgets.QPushButton("AÇ")
        self.veri_kaydet=QtWidgets.QPushButton("KAYDET")
        self.veri_temizle=QtWidgets.QPushButton("TEMİZLE")
        self.yeni_veri= QtWidgets.QPushButton("Yeni Veri Seti")
        self.message_box = QtWidgets.QMessageBox()
        self.message_box.setWindowTitle('TezV1')
        h_box=QtWidgets.QHBoxLayout()
        h_box.addWidget(self.veri_al)
        h_box.addWidget(self.veri_kaydet)
        h_box.addWidget(self.veri_temizle)
        h_box.addWidget(self.yeni_veri)
        self.timerlabel.setStyleSheet("color:mediumblue")
        self.timerlabel.setFont(QtGui.QFont('Arial',13))
        self.yeni_veri.setStyleSheet("background-color:orange")
        self.veri_al.setStyleSheet("background-color:orange")
        self.veri_kaydet.setStyleSheet("background-color:orange")
        self.veri_temizle.setStyleSheet("background-color:orange")
        self.w_apriori=QtWidgets.QPushButton("Apriori")
        self.w_eclat=QtWidgets.QPushButton("Eclat")
        self.w_arm=QtWidgets.QPushButton("A.R.M")
        self.w_prefix=QtWidgets.QPushButton("PrefixSpan")
        self.w_FpTree=QtWidgets.QPushButton("Fp-Tree")
        self.w_apriori.setStyleSheet("background-color:orange")
        self.w_arm.setStyleSheet("background-color:orange")
        self.w_eclat.setStyleSheet("background-color:orange")
        self.w_prefix.setStyleSheet("background-color:orange")
        self.w_FpTree.setStyleSheet("background-color:orange")
        self.w_arm.setFont(QtGui.QFont('Arial',14))
        self.w_eclat.setFont(QtGui.QFont('Arial', 14))
        self.w_prefix.setFont(QtGui.QFont('Arial', 14))
        self.w_apriori.setFont(QtGui.QFont('Arial', 14))
        self.w_FpTree.setFont(QtGui.QFont('Arial',14))
        self.veri_al.setFont(QtGui.QFont('Arial', 14))
        self.veri_kaydet.setFont(QtGui.QFont('Arial', 14))
        self.veri_temizle.setFont(QtGui.QFont('Arial', 14))
        self.yeni_veri.setFont(QtGui.QFont('Arial',14))
        v1_box=QtWidgets.QHBoxLayout()
        v2_box = QtWidgets.QHBoxLayout()
        h1_box=QtWidgets.QVBoxLayout()
        v1_box.addWidget(self.w_apriori)
        v1_box.addWidget(self.w_eclat)
        h1_box.addLayout(v1_box)
        v2_box.addWidget(self.w_arm)
        v2_box.addWidget(self.w_prefix)
        v2_box.addWidget(self.w_FpTree)
        h1_box.addLayout(v2_box)

        self.baslik.setStyleSheet('color:red')
        self.baslik.setFont(QtGui.QFont("Times New Roman",20))
        self.setWindowTitle("TezV1")
        v_box=QtWidgets.QVBoxLayout()
        v_box.addLayout(p)
        v_box.addWidget(self.baslik)
        v_box.addWidget(self.adres_cubugu)
        v_box.addLayout(h_box)
        v_box.addLayout(h1_box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        #LISTWIDGET LAR BU ARADA GİRİLDİ.
        self.baslik.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_baslik.setAlignment(QtCore.Qt.AlignCenter)
        self.l2_baslik.setAlignment(QtCore.Qt.AlignCenter)
        self.l1_baslik.setFont(QtGui.QFont("Times New Roman", 15))
        self.l2_baslik.setFont(QtGui.QFont("Times New Roman", 15))
        self.l1_baslik.setStyleSheet('color:red')
        self.l2_baslik.setStyleSheet('color:red')
        hbox = QtWidgets.QHBoxLayout()
        self.l1 = QtWidgets.QListWidget()
        self.l2 = QtWidgets.QListWidget()
        l1_box=QtWidgets.QVBoxLayout()
        l2_box=QtWidgets.QVBoxLayout()
        l1_box.addWidget(self.l1_baslik)
        l1_box.addWidget(self.l1)
        l2_box.addWidget(self.l2_baslik)
        l2_box.addWidget(self.l2)
        hbox.addLayout(l1_box)
        hbox.addLayout(l2_box)
        v_box.addLayout(hbox)
        #
        self.setLayout(v_box)
        self.show()
        self.veri_al.clicked.connect(self.open)
        self.veri_temizle.clicked.connect(self.sil)
        self.veri_kaydet.clicked.connect(self.kaydet)
        self.w_apriori.clicked.connect(self.apriori)
        self.w_arm.clicked.connect(self.arm)
        self.w_eclat.clicked.connect(self.eclat)
        self.w_prefix.clicked.connect(self.prefix)
        self.w_FpTree.clicked.connect(self.fp_tree)
        self.yeni_veri.clicked.connect(self.newdata)

    def open(self):
        try:
            dosya_ismi = QFileDialog.getOpenFileName(self, "DOSYA AÇ", os.getenv("HOME"))
            self.adres_cubugu.setText(dosya_ismi[0])
            dsy=dosya_ismi[0]
            #dsy=dsy.split("/")
            #dsy=dsy[-1]
            self.liste_al(dsy)
            self.message_box.setIcon(QtWidgets.QMessageBox.Information)
            self.message_box.setText("Database okundu. Lütfen devam etmek için algoritmalardan birini seçin")
            self.message_box.exec()
        except:
            self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
            self.message_box.setText("Database okuma sırasında hata ile karşılaşıldı. Tekrar deneyin !")
            self.message_box.exec()

    def sil(self):
        try:
            self.adres_cubugu.clear()
            self.database.clear()
            self.l1.clear()
            self.l2.clear()
            self.timerlabel.clear()
        except:
            pass

    def kaydet(self):
        try:
            dosya_ismi=QFileDialog.getSaveFileName(self,"DOSYA KAYDET",os.getenv("HOME"))#kaydetmek için
            self.adres_cubugu.setText(dosya_ismi[0])
            kayıt_prg=dosya_ismi[0].split("/")[-1].split(".")[-1]
            if(dosya_ismi[0] != "" and kayıt_prg == "xlsx"):
                wb=ex.Workbook("{}".format(dosya_ismi[0]))
                sf1=wb.add_worksheet('SonucSayfası')
                sf1.write(0, 0, self.kayıt_baslıgı[0][0])
                sf1.write(0, 1, self.kayıt_baslıgı[1][0])
                sayac=1
                ####ELEMAN SUPPORTU İFADERLERİ İF E BAĞLI OLARAK DEĞİŞECEK SEKİLDE YAZILACAK
                for i,j in self.cıktı:
                    S='{'+i+'}'
                    sf1.write(sayac,0,S)
                    sf1.write(sayac,1,j)
                    sayac+=1
                wb.close()
            elif(dosya_ismi[0] != "" and kayıt_prg == "txt"):
                file = open(dosya_ismi[0], "a")
                S="{}{}{}\n".format(self.kayıt_baslıgı[0][0],
                                    self.bosluk_birak(self.kayıt_baslıgı[0][0]),self.kayıt_baslıgı[1][0])
                file.writelines(S)
                for i,j in self.cıktı:
                    S = '{' + i + '}'
                    C="{}{}{}\n".format(S,self.bosluk_birak(S),str(j))
                    file.writelines(C)
                file.close()
            else:
                self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
                self.message_box.setText("Dosya kaydı .xlsx veya .txt formatında yapılmalıdır.")
                self.message_box.exec()
        except:
            self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
            self.message_box.setText("Dosya Kaydetme sırasında hata oluştu!")
            self.message_box.exec()

    def newdata(self):
        "OKUMA FORMATI AŞAĞIDAKİ GİBİ"
        "[bora,ali hakan,gaye,esin merve]/[cemal,bora,esin merve,fatma]/[fatma,ali hakan,esin merve]/[bora,fatma,gaye]/[bora,ali hakan,deniz,esin merve]/[ali hakan,fatma,gaye]/[deniz,ali hakan,bora,esin merve,fatma,gaye]/[ali hakan,bora,esin merve,fatma]/[bora,cemal,deniz,fatma]/[gaye,ali hakan,esin merve,fatma]/[esin merve,bora,deniz,fatma]"
        "[a,c,d]/[b,c,e]/[a,b,c,e]/[b,e]/[a,b,c,e]"
        try:
            self.new_data = QtWidgets.QInputDialog.getText(self, 'Input Penceresi', 'Yeni veri tabanını liste halinde giriniz ')
            self.new_data = self.new_data[0].split("/")

            dosya_ismi=QFileDialog.getSaveFileName(self,"VERİTABANI DOSYASI KAYDET",os.getenv("HOME"))#kaydetmek için
            self.adres_cubugu.setText(dosya_ismi[0]+".db")
            if len(self.new_data)>=1:
                if len(dosya_ismi[0].split("/")[-1])>=1:

                    con = sqlite3.connect(r"{}.db".format(dosya_ismi[0]))
                    cursor = con.cursor()
                    cursor.execute("CREATE TABLE IF NOT EXISTS liste1 (id TEXT, liste TEXT)")
                    con.commit()
                    kyt = 'T'
                    ct = 1
                    for i in self.new_data:
                        ready = i.replace("[","")
                        ready = ready.replace("]","")
                        item_number = kyt+str(ct)
                        cursor.execute("INSERT INTO liste1 VALUES(?,?)", (item_number, ready))
                        con.commit()
                        ct += 1
                    self.message_box.setIcon(QtWidgets.QMessageBox.Information)
                    self.message_box.setText("Yeni Veri tabanı oluşturma başarıyla tamamlandı")
                    self.message_box.exec()
                else:
                    self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
                    self.message_box.setText("Dosya isminde hata ile karşılaşıldı")
                    self.message_box.exec()
            else:
                self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
                self.message_box.setText("Hata: Veritabanı formata uygun olarak girilmedi")
                self.message_box.exec()

        except:
            self.message_box.setIcon(QtWidgets.QMessageBox.Warning)
            self.message_box.setText("Yeni Veri tabanı kaydetme sırasında hata ile karşılaşıldı")
            self.message_box.exec()
#CIKTI ALMAK İCİN KULLANDIĞIM FONKSIYONLAR
    def string_düzenle(self,*argv):
        liste=list()
        sayac=0
        for t in argv:
            liste.append("")
            for j in range(len(t)):
                liste[sayac]+=t[j]+","
            liste[sayac]=liste[sayac][:-1]
            sayac+=1
        return liste

    def str_birlestir(self,*argv):
        toplu_string = list()
        sayac = 0
        for i in argv:
            toplu_string.append("")
            for j in i:
                toplu_string[sayac] += j
            sayac += 1
        return toplu_string

    def bosluk_birak(self,eleman):
        tanımlı_bosluk=60
        bosluk=tanımlı_bosluk-len(eleman)
        return " "*bosluk

    def arm_listele(self,sonuc):
        self.l1.clear()
        self.l2.clear()
        self.cıktı=list()
        ct=1
        self.kayıt_baslıgı=[['PREMISE/CONSEQUENT'],['CONFIDENCE,LITF']]
        for i in sonuc:
            sonuc=self.string_düzenle(i.premise,i.consequent)
            i.confidence="%.4f"%i.confidence
            i.lift="%.4f"%i.lift
            t=self.str_birlestir([sonuc[0],'-->',sonuc[1]],[str(i.confidence),',',str(i.lift)])
            self.cıktı.append([t[0],t[1]])
            self.l1.insertItem(ct,str(ct)+str("##")+"\t"+str("{")+sonuc[0]+str("}")+str("--->")+str("{")+
                               sonuc[1]+str("}"))
            self.l2.insertItem(ct,str(ct)+str("##")+"\t"+str( i.confidence)+
                               "\t"+str(i.lift))
            ct+=1

    def eclat_listele(self,sonuc):
        self.l1.clear()
        self.l2.clear()
        self.cıktı=list()
        ct=1
        self.kayıt_baslıgı=[['ELEMAN'],['SUPPORTU']]
        for i in sonuc:
            s1=self.string_düzenle(i.eleman)
            self.cıktı.append([s1[0],"%.4f" %i.tid])
            self.l1.insertItem(ct,str(ct)+str("##\t")+str("{")+s1[0]+str("}"))
            self.l2.insertItem(ct,str(ct)+str("##\t")+str("%.4f" % i.tid))
            ct+=1

    def listeye_yaz(self,sonuc):
        self.l1.clear()
        self.l2.clear()
        self.cıktı=list()
        ct = 1
        self.kayıt_baslıgı=[['ELEMAN'],['SUPPORTU']]
        for i,j in sonuc:
            s1=self.string_düzenle(i)
            self.cıktı.append([s1[0],"%.4f"%j])
            self.l1.insertItem(ct,str(ct)+str("##\t")+str("{")+s1[0]+str("}"))
            self.l2.insertItem(ct,str(ct)+"##\t"+str("%.4f" %j))
            ct+=1

    def prefix_yaz(self, sonuc):
        self.l1.clear()
        self.l2.clear()
        self.cıktı = list()
        self.kayıt_baslıgı=[['ELEMAN'],['']]
        ct = 1
        for i in sonuc:
            self.cıktı.append([i,''])
            self.l1.insertItem(ct, i)
            ct += 1
#FONKSIYONLAR
    def apriori(self):
        try:
            import apriori
            self.support=self.support_sor()
            self.start_time = time.time()
            self.wt=apriori.ap(self.database,float(self.support[0]))
            self.end_time = time.time()
            self.total_time = str(self.end_time-self.start_time)[0:9]
            self.timerlabel.setText("ÇALIŞMA SÜRESİ:"+str(self.total_time)+"s")
            self.l1_baslik.setText("ELEMAN")
            self.l2_baslik.setText("SUPPORTU")
            self.listeye_yaz(self.wt)
        except:
            pass

    def arm(self):
        try:
            import arm
            import apriori
            self.support=self.support_sor()
            self.conf = self.conf_sor()
            self.start_time = time.time()
            snc=apriori.ap(self.database,float(self.support[0]))
            self.wt = arm.arm_fonc(snc, float(self.conf[0]))
            self.end_time = time.time()
            self.total_time = str(self.end_time-self.start_time)[0:9]
            self.timerlabel.setText("ÇALIŞMA SÜRESİ:"+str(self.total_time)+"s")
            self.l1_baslik.setText("PREMISE/CONSEQUENT")
            self.l2_baslik.setText("CONFIDENCE/LIFT")

            self.arm_listele(self.wt)
        except:
            pass

    def eclat(self):
        try:
            """
            import eclat
            self.support=self.support_sor()
            self.wt=eclat.ec(self.database,float(self.support[0]))
            self.l1_baslik.setText("ELEMAN")
            self.l2_baslik.setText("SUPPORTU")
            self.eclat_listele(self.wt)
            """
            import ec2
            self.support = self.support_sor()
            self.start_time = time.time()
            self.wt = ec2.ec(self.database, float(self.support[0]))
            self.end_time = time.time()
            self.total_time = str(self.end_time-self.start_time)[0:9]
            self.timerlabel.setText("ÇALIŞMA SÜRESİ:"+str(self.total_time)+"s")
            self.l1_baslik.setText("ELEMAN")
            self.l2_baslik.setText("SUPPORTU")
            self.eclat_listele(self.wt)
        except:
            pass

    def prefix(self):
        try:
            import prefix_span
            self.support = self.support_sor()
            self.start_time = time.time()
            self.wt = prefix_span.pSPAN(self.database, float(self.support[0]))
            self.end_time = time.time()
            self.total_time = str(self.end_time-self.start_time)[0:9]
            self.timerlabel.setText("ÇALIŞMA SÜRESİ:"+str(self.total_time)+"s")
            self.l1_baslik.setText("PrefixSpan SONUCLAR")
            self.l2_baslik.clear()
            self.prefix_yaz(self.wt)
        except:
            pass

    def fp_tree(self):
        try:
            import Fp_Tree2
            self.support = self.support_sor()
            self.start_time = time.time()
            self.wt = Fp_Tree2.fptree(self.database, float(self.support[0]))
            self.end_time = time.time()
            self.total_time = str(self.end_time-self.start_time)[0:9]
            self.timerlabel.setText("ÇALIŞMA SÜRESİ:"+str(self.total_time)+"s")
            self.l1_baslik.setText("Fp-Tree Elemanlar")
            self.l2_baslik.setText("Eleman Supportu")
            self.listeye_yaz(self.wt)
        except:
            pass

    def support_sor(self):
        sup1 = QtWidgets.QInputDialog.getText(self, 'Input Penceresi', 'Minimum Support Değerini giriniz:')
        return sup1

    def conf_sor(self):
        conf1 = QtWidgets.QInputDialog.getText(self, 'Input Penceresi', 'Minimum Conf Değerini giriniz:')
        return conf1

    def liste_al(self,baglantı_adi):
        con = sqlite3.connect(baglantı_adi)
        ## İLK TABLE I ALIYORUZ
        cursor = con.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        tables = tables[0][0]
        ## İLK TABLE I DATABASE E ATIYORUZ
        database = pd.read_sql_query(f"SELECT * from {tables}", con)
        ##SADECE DATANIN KAYITLI OLDUĞU SÜTUNU ALIYORUZ. NUMARALANDIRMA SÜTUNU ZATEN PANDAS TAN GELECEK.
        sütun = len(database.columns)
        if sütun > 1:
            for i in range(sütun - 1):
                database = database.drop(database.columns[0], axis=1)
        database = database.values.tolist()
        for num, element in enumerate(database):
            database[num] = element[0].split(',')
        self.database = database
        """        
        import sqlite3
        con = sqlite3.connect(baglantı_adi)
        cursor = con.cursor()
        cursor.execute("SELECT *FROM liste1")
        liste = cursor.fetchall()
        self.main_list = [[0 for i in range(2)] for j in range(len(liste))]
        self.main1_list = []
        a = 0
        for i, j in liste:
            b = 0
            self.main_list[a][b] = i
            self.main1_list.append(j.split(","))
            b += 1
            self.main_list[a][b] = j.split(",")
            a += 1"""
#####################################################################################
app=QtWidgets.QApplication(sys.argv)
uyg=ana_ekran()
sys.exit(app.exec_())








