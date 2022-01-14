# -*- coding: utf-8 -*-
import numpy as np
class ortak_islemler():
    def eleman_listesi(self,lst):
        liste=[]
        for i in lst:
            liste=list(set(i).union(liste))
        liste.sort()
        return liste
    def minsup_kontrol(self,deger,minsup):
        if(deger>=minsup):
            return True
    def frequent_finder(self,deger,liste):
        ct=0
        for i in liste:
            index=np.in1d(deger,i)
            index=list(index)
            if (all(index)==True):
                ct+=1
        ct/=len(liste)
        return ct
    def same_control(self,eleman,liste):
        t=0
        for i in liste:
            index=np.in1d(eleman[0],i[0])
            if(all(index)==True):
                t=1
                break
        return t