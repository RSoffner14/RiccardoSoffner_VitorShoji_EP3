# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:42:25 2015

@author: Riccardo
"""

def alimentos_():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    InformacoesNutricionaisCalPorGram={}
    for contador,linha in enumerate(leitura_a[1:]):
                
        partes = linha.split(',')
        cemgramas=int(partes[1])
        calorias=float(partes[2])
        
        InformacoesNutricionaisCalPorGram[partes[0]]=calorias/cemgramas
    return InformacoesNutricionaisCalPorGram
alimentos_()

def alimentos_proteinas():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    InformacoesNutricionaisCalPorGram={}
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        cemgramas=int(partes[1])
        proteinas=float(partes[3])
        InformacoesNutricionaisCalPorGram[partes[0]]=proteinas/cemgramas
    return InformacoesNutricionaisCalPorGram
alimentos_proteinas()

def alimentos_carboidratos():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    InformacoesNutricionaisCalPorGram={}
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        cemgramas=int(partes[1])
        carboidratos=float(partes[4])
        InformacoesNutricionaisCalPorGram[partes[0]]=carboidratos/cemgramas
    return InformacoesNutricionaisCalPorGram
alimentos_carboidratos()

def alimentos_gordura():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    InformacoesNutricionaisCalPorGram={}
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        cemgramas=int(partes[1])
        gordura=float(partes[5])
        InformacoesNutricionaisCalPorGram[partes[0]]=gordura/cemgramas
    return InformacoesNutricionaisCalPorGram
alimentos_gordura()

def proteinas():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        proteinas=float(partes[3])
        return proteinas
proteinas()

def carboidratos():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        carboidratos=float(partes[4])
        return carboidratos
carboidratos()
    
    
def gordura():
    alimentos=open("alimentos.csv.csv","r")
    leitura_a=alimentos.readlines()
    for contador,linha in enumerate(leitura_a[1:]):
        partes=linha.split(',')
        gordura=float(partes[5])
        return gordura
gordura()


