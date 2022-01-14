# -*- coding: utf-8 -*-
import numpy as np
from copy import deepcopy
import itertools


def fptree(data, support):
    class islemler():
        def eleman_listesi(self, liste):
            elemanlar = dict()
            for i in liste:
                for j in i:
                    if (np.in1d(j, elemanlar) == False):
                        elemanlar[j] = None
            return elemanlar
        #############################################################
        def ordered_items(self, listem, support):
            liste = deepcopy(listem)
            gecen_elemanlar = dict()
            # Eleman Listesinin Bulunması
            elemanlar = self.eleman_listesi(liste)
            for i in elemanlar.keys():
                # Eleman listesi üzerinden sıklık taraması
                # Sıklığı yeterli değilse listeden atılacak.
                ct = 0
                for j in liste:
                    if (np.in1d(i, j) == True):
                        ct += 1
                if (ct >= support):
                    gecen_elemanlar[i] = ct
                else:
                    for m in liste:
                        try:
                            m.remove(i)
                        except:
                            pass

            ordered_list = self.sırala(gecen_elemanlar, liste)
            ordered_list = self.düzenle(ordered_list, gecen_elemanlar)
            return ordered_list, gecen_elemanlar
        #############################################################
        def düzenle(self, liste, gecen_elemanlar):
            for i in liste:
                for j in range(len(i)):
                    for k in range(j + 1, len(i)):
                        if (gecen_elemanlar[i[j]] == gecen_elemanlar[i[k]]):
                            sorted_list = [i[j], i[k]]
                            sorted_list.sort()
                            i[j] = sorted_list[0]
                            i[k] = sorted_list[1]

            return liste
        #############################################################
        def sırala(self, elemanlar, liste):
            # Burada sıklığı yeterli olan elemanları sıklığına göre sıraya dizeceğiz.
            for i in liste:
                for j in range(len(i) - 1):
                    for m in range(j + 1, len(i)):
                        if (elemanlar[i[j]] < elemanlar[i[m]]):
                            i[j], i[m] = i[m], i[j]
            return liste
        #############################################################
        def frequent_itemlist(self, ordered_list, items, support):
            output = list()
            for i in items.keys():
                output.append([[i], items[i]])
                to_node_way = list()
                for j in ordered_list:
                    if (any(np.in1d(i, j))):
                        item_index = j.index(i)
                        to_node_way = self.listeye_ekle(to_node_way, j[0:item_index])
                passed_elements = sorted(set([m for m in to_node_way if to_node_way.count(m) >= support]))
                passed_dict = dict()
                for m in passed_elements:
                    passed_dict[m] = to_node_way.count(m)
                output = self.mine_elements(i, passed_dict, output, ordered_list, support)
            return output
        #############################################################
        def listeye_ekle(self, node_list, elemanlar):
            for i in elemanlar:
                node_list.append(i)
            return node_list
        #############################################################
        def mine_elements(self, node, frequent_elements, output, database, support):
            len_elements = len(frequent_elements) + 1
            for m in range(1, len_elements):
                items = list(itertools.combinations(frequent_elements, m))
                for i in items:
                    item1 = self.TupleToStr(i)
                    m = item1 + "," + node
                    m = m.split(",")
                    if (self.check(m, database) >= support):
                        output.append([[item1 + "," + node], frequent_elements[item1.split(",")[0]]])
            return output
        #############################################################
        def TupleToStr(self, demet):
            con_str = ''
            for i in demet:
                con_str += i
                con_str += ","
            con_str = con_str[:-1]
            return con_str
        #################################################################
        def check(self, m, database):
            ct = 0
            for i in database:
                if (all(np.in1d(m, i))):
                    ct += 1
            return ct
    #################################################################

    islem = islemler()
    ordered_list, items = islem.ordered_items(data, support)
    output = islem.frequent_itemlist(ordered_list, items, support)
    return output

#BU SATIR SADECE BU FONKSİYON CALISTIRILACAĞI ZAMAN AKTİF EDİLİR
"""
liste1 = [['f', 'a', 'c', 'd', 'g', 'i', 'm', 'p'],
          ['a', 'b', 'c', 'f', 'l', 'm', 'o'],
          ['b', 'f', 'h', 'j', 'o'],
          ['b', 'c', 'k', 's', 'p'],
          ['a', 'f', 'c', 'e', 'l', 'p', 'm', 'n']]
liste2 = [['bora', 'ali hakan', 'gaye', 'esin merve'],
          ['cemal', 'bora', 'esin merve', 'fatma'],
          ['fatma', 'ali hakan', 'esin merve'],
          ['bora', 'fatma', 'gaye'],
          ['bora', 'ali hakan', 'deniz', 'esin merve'],
          ['ali hakan', 'fatma', 'gaye'],
          ['deniz', 'ali hakan', 'bora', 'esin merve', 'fatma', 'gaye'],
          ['ali hakan', 'bora', 'esin merve', 'fatma'],
          ['bora', 'cemal', 'deniz', 'fatma'],
          ['gaye', 'ali hakan', 'esin merve', 'fatma'],
          ['esin merve', 'bora', 'deniz', 'fatma']]
liste3 = [['a', 'c', 'd'],
          ['b', 'c', 'e'],
          ['a', 'b', 'c', 'e'],
          ['b', 'e'],
          ['a', 'b', 'c', 'e']]
cıktı = fptree(liste2, 1.1)
print(len(cıktı))
ct = 1
for i in cıktı:
    print(ct, ".", i)
    ct += 1
sayac = 1
"""
