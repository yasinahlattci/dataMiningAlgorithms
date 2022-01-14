# -*- coding: utf-8 -*-
def ec(listem, minsup):
    import numpy as np
    import  ortak_class

    class eclat(ortak_class.ortak_islemler):

        class kayıt():
            def __init__(self, eleman, tid):
                self.eleman = eleman
                self.tid = tid

        ##############################################
        def tid_list(self, eleman, liste):
            tid_x = list()
            for i in eleman:
                index = list()
                sayac = 1
                for j in liste:
                    if (np.in1d(i, j)):
                        index.append(sayac)
                    sayac += 1
                tid_x.append(self.kayıt(i, index))
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
                if (nstack != []):
                    nstack.pop(0)
            return nstack

        ##############################################
        def intersect(self, k1, k2):
            intersect_list = list(set.intersection(set(k1), set(k2)))
            return intersect_list

        ##############################################
        def eclat_main(self, elem, ana_liste, sup, uzunluk, sonuc_listesi):
            n_list = []
            t = self.stack_bul(elem, ana_liste)
            for j in t:
                sup_hesap = len(islem.intersect(elem.tid, j.tid)) / uzunluk
                if sup_hesap >= sup:
                    d = list(elem.eleman)
                    d.append(j.eleman[0])
                    n_list.append(self.kayıt(d, self.intersect(elem.tid, j.tid)))
                    if self.ekli_mi(d, sonuc_listesi) == False:
                        sonuc_listesi.append(self.kayıt(d, sup_hesap))
            if len(n_list) > 1:
                for i in n_list:
                    sonuc_listesi = self.eclat_main(i, ana_liste, sup, uzunluk, sonuc_listesi)

            return sonuc_listesi

        ##############################################
        def ekli_mi(self, eleman, liste):
            yanlıs = False
            for i in liste:
                if (all(np.in1d(eleman, i.eleman)) == True):
                    if (len(eleman) == len(i.eleman)):
                        yanlıs = True
                        break
            return yanlıs
        ##############################################


    islem = eclat()
    liste_boyu = len(listem)
    main_list = list()
    sonuc_list = list()
    tid_x = islem.tid_list(islem.eleman_listesi(listem), listem)

    for i in tid_x:
        sup_hesap = len(islem.intersect(i.tid, i.tid)) / liste_boyu
        if (sup_hesap > minsup):
            main_list.append(islem.kayıt([i.eleman], i.tid))
    for i in main_list:
        sonuc_list.append(islem.kayıt(i.eleman, len(i.tid) / liste_boyu))
        sonuc_list = islem.eclat_main(i, main_list, minsup, liste_boyu, sonuc_list)
    return sonuc_list


# BU SATIR SADECE BU FONKSİYON CALISTIRILACAĞI ZAMAN AKTİF EDİLİR
l2 = [['a', 'c', 'd'], ['b', 'c', 'e'], ['a', 'b', 'c', 'e'], ['b', 'e'], ['a', 'b', 'c', 'e']]
l1 = [['bora', 'ali hakan', 'gaye', 'esin merve'], ['cemal', 'bora', 'esin merve', 'fatma'],
      ['fatma', 'ali hakan', 'esin merve'], ['bora', 'fatma', 'gaye'], ['bora', 'ali hakan', 'deniz', 'esin merve'],
      ['ali hakan', 'fatma', 'gaye'], ['deniz', 'ali hakan', 'bora', 'esin merve', 'fatma', 'gaye'],
      ['ali hakan', 'bora', 'esin merve', 'fatma'], ['bora', 'cemal', 'deniz', 'fatma'],
      ['gaye', 'ali hakan', 'esin merve', 'fatma'], ['esin merve', 'bora', 'deniz', 'fatma']]
t = ec(l1, 0.1)





