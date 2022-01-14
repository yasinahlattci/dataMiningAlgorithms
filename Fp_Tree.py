# -*- coding: utf-8 -*-
import numpy as np
from copy import deepcopy
import itertools

def fptree(data, support):
    class islemler():
        def eleman_listesi(self,liste):
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
            ordered_list = self.düzenle(ordered_list)
            return ordered_list, gecen_elemanlar
        #############################################################
        def düzenle(self, liste):
            for i in range(1, len(liste)):
                for j in range(0, i):
                    if (all(np.in1d(liste[i], liste[j])) == True and len(liste[i]) == len(liste[j])):
                        # Aynı elemanları setleri ortak düzene koyduk
                        liste[i] = liste[j]
                        break
                    else:
                        # Elemanlarda fark varsa prefixlere bakacağız. Aynı prefixlere sahip setleri eşitleyeceğiz.
                        uzunluk = min(len(liste[i]), len(liste[j]))
                        uzunluk -= 1
                        for m in range(uzunluk, -1, -1):
                            if (all(np.in1d(liste[i][0:m], liste[j][0:m])) == True
                                    and liste[i][0:m] != [] and liste[j][0:m] != []):
                                liste[i][0:m] = liste[j][0:m]
                                break
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
                output.append([i, items[i]])
                to_node_way = list()
                for j in ordered_list:
                    if (any(np.in1d(i, j))):
                        item_index = j.index(i)
                        to_node_way = self.listeye_ekle(to_node_way, j[0:item_index])
                passed_elements = sorted(set([m for m in to_node_way if to_node_way.count(m) >= support]))
                passed_dict = dict()
                for m in passed_elements:
                    passed_dict[m] = to_node_way.count(m)
                output = self.mine_elements(i, passed_dict, output)
            return output
        #############################################################
        def listeye_ekle(self, node_list, elemanlar):
            for i in elemanlar:
                node_list.append(i)
            return node_list
        #############################################################
        def mine_elements(self, node, frequent_elements, output):
            len_elements = len(frequent_elements) + 1
            for m in range(1, len_elements):
                items = list(itertools.combinations(frequent_elements, m))
                for i in items:
                    item1 = self.TupleToStr(i)
                    output.append([item1 + "," + node, frequent_elements[item1.split(",")[0]]])
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
    islem = islemler()
    ordered_list, items = islem.ordered_items(data, support)
    output = islem.frequent_itemlist(ordered_list, items, support)
    return output

"""
liste1=[['f','a','c','d','g','i','m','p'],
       ['a','b','c','f','l','m','o'],
       ['b','f','h','j','o'],
       ['b','c','k','s','p'],
       ['a','f','c','e','l','p','m','n']]
liste2=[['bora', 'ali hakan', 'gaye', 'esin merve'],
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
liste3=[['a','c','d'],
        ['b','c','e'],
        ['a','b','c','e'],
        ['b','e'],
        ['a','b','c','e']]
cıktı = fptree(liste2, 1.1)
sayac = 1
for i in cıktı:
    print(sayac,"-->", i)
    sayac+=1
"""