# -*- coding: utf-8 -*-
import numpy as np
from copy import deepcopy
def pSPAN(data, support):

    class islemler():

        def find_suffix(self, prefix, liste, _hold):
            """
            Burada suffix bulma işlemi yapıyoruz. Örneğin ['a','abc','ac','d','cf'] de prefix 'a' ise
            buradan dönecek değer ['abc','ac','d','cf']

            Liste -> data. Data her seferinde değişiyor. Örneğin başlangıcta <a> projected-db için dönüş yaptık.
            <ab> projected-db yi bulmak için bu fonksiyona find_suffix('b', new_db, ' ') gönderiyoruz.

            _hold -> Database de '_x' seklinde bir değer var ise burada suffix bulur iken position holder in yerine
            koyuluyor
            find_suffix ana fonksiyon. FindPH ve FindSF yardımcı.
            """
            full_list = list()
            innerlist = deepcopy(liste)
            if (len(prefix) > 1):
                # _ yerine yerini tuttuğu şeyi yazıyoruz.
                PH = list(prefix)
                PH.remove('_')
                PH.insert(0, _hold)
                PH = self.listToString(PH)
                for i in innerlist:
                    for j in i:
                        if (all(np.in1d(list(prefix), list(j))) == True or all(np.in1d(list(PH), list(j))) == True):
                            sonuc = self.findPH(prefix, j, PH, i)
                            if (sonuc[1] == False):
                                full_list.append(sonuc[0])
                            break
                        else:
                            continue

            elif (len(prefix) == 1):
                for i in innerlist:
                    for j in i:
                        if (np.in1d(list(prefix), list(j)) == True and np.in1d('_', list(j)) == False):
                            sonuc = self.findSF(prefix, j, i)
                            if (sonuc[1] == False):
                                full_list.append(sonuc[0])
                                break
            else:
                pass
            return full_list
        ##############################################
        def findPH(self, prefix, j, PH, i):
            """
            Eğer position holder var ise suffixi bulmak için bu fonksiyon çalışıyor.
            Aynı zamanda bu fonksiyon eğer len(prefix) > 1 olduğu durumlar çalışır.
            """
            bosliste = False
            if (len(j) > len(prefix) or len(PH) > len(prefix)):
                d_index = i.index(j)
                d_index += 1
                j = list(j)
                # burada if elif e gerek yok gibi.
                # Sadece islemi yazsak yeter gibi duruyor bakacağız.
                if (all(np.in1d(list(PH), list(j))) == True):
                    for _ in range(len(PH)):
                        j.pop(0)
                    j.insert(0, '_')
                    j = self.listToString(j)
                    for _ in range(d_index):
                        i.pop(0)
                    i.insert(0, j)
                elif (all(np.in1d(list(prefix), list(j))) == True):
                    for _ in range(len(prefix)):
                        j.pop(0)
                    j.insert(0, '_')
                    j = self.listToString(j)
                    for _ in range(d_index):
                        i.pop(0)
                    i.insert(0, j)
                else:
                    pass
            elif (len(j) == len(prefix) or len(PH) == len(prefix)):
                d_index = i.index(j)
                d_index += 1
                for _ in range(d_index):
                    i.pop(0)
            else:
                pass
            if (i == []):
                bosliste = True

            return [i, bosliste]
        ##############################################
        def findSF(self, prefix, j, i):
            """
            len(prefix)  = 1 olduğu durumlar için suffix bulmaya yardımcı fonksiyon.
            """
            bosliste = False
            j_index = j.index(prefix)
            j_index += 1
            len_j = len(j)
            i_index = i.index(j)
            i_index += 1
            j = list(j)
            if (len_j == j_index):
                for _ in range(i_index):
                    i.pop(0)
            else:
                for _ in range(j_index):
                    j.pop(0)
                j.insert(0, '_')
                j = self.listToString(j)
                for _ in range(i_index):
                    i.pop(0)
                i.insert(0, j)
            if (i == []):
                bosliste = True
            return [i, bosliste]
        ##############################################
        def listToString(self, s):
            "Verilen listeyi stringe çevrilmiş halde döndürür."
            str1 = " "
            return (str1.join(s)).replace(" ", "")
        ##############################################
        def frequentfinder(self, liste, sup, _for):
            """
            Gelen database i tarayarak sık-öğe setlerini bulur.
            liste -> find_suffix den cıkan database
            sup -> Dışarıdan girilen support değeri
            _for -> Position holder bilgisini taşır.
            """
            mined_list = list()
            innerlist = deepcopy(liste)

            if len(innerlist) < sup:
                "Listenin elemanı supporttan az ise frequent item çıkamaz boş küme döneriz."
                return mined_list
            else:
                out, innerlist = self.position_holder(liste, sup, _for)
                innerlist = self.liste_bulucu(innerlist)
                out2 = sorted(set([m for m in innerlist if innerlist.count(m) >= sup]))
                out = out + out2
                for i in out:
                    mined_list.append(i)

            return mined_list
        ##############################################
        def position_holder(self, liste, sup, _for):
            """Database de position holderla karsılaşılırsa bu fonksiyon çalısır. Position holderli bütün elemanları
             ayırır ve databaseden atar. Ayrılan position holderlı elemanlarda sık-öğe arar.
             Varsa sık öğe seti ve position-holder lar atılmış sekilde database i döner.
            """
            liste = deepcopy(liste)
            pholder = list()
            for i in liste:
                if (np.in1d('_', list(i[0]))):
                    pholder.append(i[0])
                    i.pop(0)
            npholder = deepcopy(pholder)
            ct = 0
            for i in npholder:
                m = list(i)
                m.remove('_')
                m.insert(0, _for)
                m = self.listToString(m)
                npholder[ct] = m
                del m
                ct += 1
            for i in liste:
                for j in i:
                    for m in npholder:
                        if (all(np.in1d(list(m), list(j))) == True):
                            pholder.append(m)
            ct = 0
            for i in pholder:
                if (i[0] != '_'):
                    m = list(i)
                    m.remove(i[0])
                    m.insert(0, '_')
                    m = self.listToString(m)
                    pholder[ct] = m
                ct += 1
            out = sorted(set([m for m in pholder if pholder.count(m) >= sup]))

            return out, liste
        ##############################################
        def liste_bulucu(self, innerlist):
            """Database deki elemanların her satır başı özgün elemanlarını bulur.
            Aynı satırda 2 tane aynı eleman varsa bir tanesini yazar.
            frequent_finder da bu cıktı_liste taranıp sık-öğe elemanlar bulunacak."""
            cıktı_liste = list()
            for i in innerlist:
                x = self.unique_list(i)
                for m in x:
                    cıktı_liste.append(m)
            return cıktı_liste
        ##############################################
        def unique_list(self, liste):
            bs = list()
            for i in liste:
                for j in i:
                    if (bs.count(j) == 0):
                        bs.append(j)
            if (self.check(bs) == False):
                bs = self.unique_list(bs)
            return bs
        ##############################################
        def check(self, liste):
            state = True
            for i in liste:
                if (len(i) > 1):
                    state = False
                    break
            return state
        ##############################################
        def mined(self, element, pholder, pre_mined):
            m = list(element)
            if (np.in1d('_', m) == True):
                pm_list = list(pre_mined)
                pm_list.remove(pholder)
                m.remove('_')
                m.insert(0, pholder)
                m.insert(0, '(')
                m.append(')')
                m = self.listToString(m)
                pm_list = self.listToString(pm_list)
                m = pm_list + m
            else:
                m.insert(0, pre_mined)
                m = self.listToString(m)
            return m
        ##############################################
        def dongu(self, sonuc, data, hold, sup, sonuc_listesi, pre_mined):
            """
            Bütün islemler sırası ile bu fonksiyonda döner.

            """
            for i in sonuc:
                mine = self.mined(i, hold, pre_mined)
                sonuc_listesi.append(mine)
                new_db = self.find_suffix(i, data, hold)
                hold = i

                new_elements = self.frequentfinder(new_db, sup, hold)
                if (len(new_elements)>0):
                    self.dongu(new_elements, new_db, hold, sup, sonuc_listesi, mine)

            return sonuc_listesi
        ##############################################
        def pretty(self, cıktı):
            "Sonucları çıktı için göndermeden önce daha güzel bir hale getirir."
            cıktı_listesi = list()
            for i in cıktı:
                m = list(i)
                m.insert(0,'<')
                m.append('>')
                m = self.listToString(m)
                cıktı_listesi.append(m)
            return cıktı_listesi

    islem = islemler()
    sonuc = islem.frequentfinder(data, support, '')
    sonuc_listesi = list()
    hold = ''
    empty= ''
    sonuc_listesi = islem.dongu(sonuc, data, hold, support, sonuc_listesi, empty)
    sonuc_listesi = islem.pretty(sonuc_listesi)
    return sonuc_listesi

"""
BU SATIR SADECE BU FONKSİYON CALISTIRILACAĞI ZAMAN AKTİF EDİLİR
dbase=[['a','abc','ac','d','cf'],
       ['ad','c','bc','ae'],
       ['ef','ab','df','c', 'b'],
       ['e','g','af','c','b','c']]
sup = 2
pSPAN(dbase, sup)
"""