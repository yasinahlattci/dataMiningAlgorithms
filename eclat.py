# -*- coding: utf-8 -*-
def ec(listem, minsup):
    import numpy as np
    import ortak_class
    class eclat(ortak_class.ortak_islemler):

        class kayıt():
            def __init__(self,eleman,tid):
                self.eleman=eleman
                self.tid=tid
        ##############################################
        def tid_list(self, eleman, liste):
            tid_x=list()
            sayac=0
            for i in eleman:
                tid_x.append(self.kayıt(i,[]))
                for j in liste:
                    index = any(np.in1d(i, j))
                    tid_x[sayac].tid.append(index)
                sayac+=1
            return tid_x
        ##############################################
        def stack_bul(self, deger, liste):
            nstack = list(liste)
            d = deger.eleman[-1]
            ct = 1
            for i in nstack:
                if (i.eleman == [d]):
                    break
                else:
                    ct += 1
            for i in range(ct):
                if (nstack!=[]):
                    nstack.pop(0)
            return nstack
        ##############################################
        def intersect(self, k1, k2):
            t = len(k1)
            s=0
            ortak = []
            for i in range(t):
                if (k1[s] == k2[s]==True):
                    ortak.append(1)
                else:
                    ortak.append(0)
                s += 1
            return ortak
        ##############################################
        def eclat_main(self,liste,ana_liste, sup, uzunluk, sonuc_listesi):
            n_list=[]
            for i in liste:
                t=self.stack_bul(i, ana_liste)
                """
                t nin tid özelliği olmasa da olur. ana_liste den o özelliği cekebiliriz.
                
                print("T Yİ YAZDIRIYORUM")
                for m in t:
                    print(m.eleman)
                """
                for j in t:
                    sup_hesap = islem.intersect(i.tid, j.tid).count(1) / uzunluk
                    if (sup_hesap >= sup):
                        d=list(i.eleman)
                        d.append(j.eleman[0])
                        n_list.append(self.kayıt(d,self.intersect(i.tid,j.tid)))
                        if (self.ekli_mi(d,sonuc_listesi) == False):
                            sonuc_listesi.append(self.kayıt(d, sup_hesap))
                if (len(n_list) != 1):
                    self.eclat_main(n_list, ana_liste, sup, uzunluk, sonuc_listesi)
            return sonuc_listesi
        ##############################################
        def ekli_mi(self,eleman,liste):
            yanlıs=False
            for i in liste:
                if(all(np.in1d(eleman,i.eleman))==True):
                    if (len(eleman)==len(i.eleman)):
                        yanlıs=True
                        break
            return yanlıs
        ##############################################
    islem=eclat()
    liste_boyu = len(listem)
    main_list=list()
    sonuc_list=list()
    tid_x=islem.tid_list(islem.eleman_listesi(listem),listem)
    for i in tid_x:
        sup_hesap=islem.intersect(i.tid,i.tid).count(1)/liste_boyu
        if(sup_hesap>minsup):
            main_list.append(islem.kayıt([i.eleman],i.tid))
            sonuc_list.append(islem.kayıt([i.eleman],sup_hesap))
            print(i.eleman)
    #dict_main=dict(main_list) dictionary seklinde ekleyip verileri burdan alma düsüncem var.
    x = islem.eclat_main(main_list, main_list, minsup, liste_boyu, sonuc_list)
    return x


#BU SATIR SADECE BU FONKSİYON CALISTIRILACAĞI ZAMAN AKTİF EDİLİR
l2=[['a','c','d'],['b','c','e'],['a','b','c','e'],['b','e'],['a','b','c','e']]
l1=[['bora', 'ali hakan', 'gaye', 'esin merve'], ['cemal', 'bora', 'esin merve', 'fatma'], ['fatma', 'ali hakan', 'esin merve'], ['bora', 'fatma', 'gaye'], ['bora', 'ali hakan', 'deniz', 'esin merve'], ['ali hakan', 'fatma', 'gaye'], ['deniz', 'ali hakan', 'bora', 'esin merve', 'fatma', 'gaye'], ['ali hakan', 'bora', 'esin merve', 'fatma'], ['bora', 'cemal', 'deniz', 'fatma'], ['gaye', 'ali hakan', 'esin merve', 'fatma'], ['esin merve', 'bora', 'deniz', 'fatma']]
t=ec(l1,0.1)





