# -*- coding: utf-8 -*-
def ap(listem,min_sup):
    import ortak_class

    class apriori(ortak_class.ortak_islemler):
        #Ortak class dan eleman listesi bulma,minsup kontrol,frequent kontrol özelliklerini inherit aldık..
        #simdi apriori ye özgü olanları burda ekstradan tanımlayacağız.
        def birlestir(self,girdi1,girdi2):
            t = list(set().union(girdi1, girdi2))
            return t
    islem=apriori()
    liste1=islem.eleman_listesi(listem)
    first_row=[]
    for i in liste1:
        relsup=islem.frequent_finder(i,listem)
        if(islem.minsup_kontrol(relsup,min_sup)==True):
            first_row.append([[i],relsup])
    t=0
    devam=True
    sonuc_listesi=list(first_row)
    aktif_liste=list(first_row)
    while(devam==True):
        bos_liste = []
        say = 0
        for i,j in aktif_liste:
            say+=1
            for k,m in aktif_liste[say:]:
                t=islem.birlestir(i,k)
                rs=islem.frequent_finder(t,listem)
                if (islem.minsup_kontrol(rs, min_sup) == True):
                    if (len(t)==(len(aktif_liste[0][0])+1)):
                        if(islem.same_control([t,rs],sonuc_listesi)==0):
                            #w=str(t)
                            #sonuc_dict[w]=rs
                            sonuc_listesi.append([t,rs])
                            bos_liste.append([t,rs])
        del aktif_liste
        aktif_liste=list(bos_liste)
        del bos_liste
        if (len(aktif_liste)<=1):
            devam=False
    return sonuc_listesi

"""#BU SATIR SADECE BU FONKSİYON CALISTIRILACAĞI ZAMAN AKTİF EDİLİR
l1=[['bora', 'ali hakan', 'gaye', 'esin merve'], ['cemal', 'bora', 'esin merve', 'fatma'], ['fatma', 'ali hakan', 'esin merve'], ['bora', 'fatma', 'gaye'], ['bora', 'ali hakan', 'deniz', 'esin merve'], ['ali hakan', 'fatma', 'gaye'], ['deniz', 'ali hakan', 'bora', 'esin merve', 'fatma', 'gaye'], ['ali hakan', 'bora', 'esin merve', 'fatma'], ['bora', 'cemal', 'deniz', 'fatma'], ['gaye', 'ali hakan', 'esin merve', 'fatma'], ['esin merve', 'bora', 'deniz', 'fatma']]
l2=[['a','c','d'],['b','c','e'],['a','b','c','e'],['b','e'],['a','b','c','e']]
l3=[['f','a','c','d','g','i','m','p'],['a','b','c','f','l','m','o'],['b','f','h','j','o'],['b','c','k','s','p'],['a','f','c','e','l','p','m','n']]
wt=ap(l3,0.6)"""








