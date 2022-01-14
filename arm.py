# -*- coding: utf-8 -*-
import numpy as np
def arm_fonc(apriori_sonucları,min_conf):
    class arm_islemler():

        class sonuc_kaydet():

            def __init__(self,premise,consequent,confidence,lift):
                self.premise=premise
                self.consequent=consequent
                self.confidence=confidence
                self.lift=lift
        ##############################################
        def conf_hesap(self,girdi,min_conf):
            sonuc_listesi=[]
            for i in girdi:
                premise=i[0]
                girdi2=self.kalan(premise,girdi)
                for j in girdi2:
                    consequent=j[0]
                    birlesik=self.birlestir(premise,consequent)
                    conf=self.birlesik_support(birlesik,girdi)/i[1]
                    if (conf>min_conf):
                        lft=self.lift_hesap(consequent,girdi,conf)
                        sonuc_listesi.append(self.sonuc_kaydet(premise,consequent,conf,lft))
            return sonuc_listesi
        ##############################################
        def lift_hesap(self,consequent,girdi,conf):
            c_sup=self.birlesik_support(consequent,girdi)
            lift=conf/c_sup
            return lift
        ##############################################
        def kalan(self,deger,liste):
            kln=list(liste)
            atılan = []
            for i in kln:
                index = np.in1d(deger, i[0])
                if (any(index) == True):
                    atılan.append(i)
            for i in atılan:
                kln.remove(i)
            return kln
        ##############################################
        def birlestir(self,girdi1,girdi2):
            t = list(set().union(girdi1, girdi2))
            return t
        ##############################################
        def birlesik_support(self,eleman,liste):
            s=0
            for i in liste:

                index=np.in1d(eleman,i[0])
                print(index)
                if(all(index)==True):
                    s=i[1]
                    break
            print(s)
            return s
        ##############################################

    islem=arm_islemler()
    sonuc=islem.conf_hesap(apriori_sonucları,min_conf)
    return sonuc


#BU SATIR SADECE BU FONKSİYON CALISTIRILACAĞI ZAMAN AKTİF EDİLİR
l1=[[['c'], 0.8], [['b'], 0.8], [['a'], 0.6], [['e'], 0.8], [['c', 'b'], 0.6], [['c', 'a'], 0.6], [['c', 'e'], 0.6], [['b', 'a'], 0.4], [['b', 'e'], 0.8], [['a', 'e'], 0.4], [['c', 'b', 'a'], 0.4], [['c', 'b', 'e'], 0.6], [['c', 'a', 'e'], 0.4], [['b', 'a', 'e'], 0.4], [['c', 'b', 'a', 'e'], 0.4]]
arm_fonc(l1,0.95)

