# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 10:26:36 2015

@author: Riccardo
"""

import matplotlib.pyplot as plt

                                 # precisa chamaro o arquivo de excel

def FuncaoHomem (peso, altura, idade):           #definição das funções
    return 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)

def FuncaoMulher(peso, altura, idade):
    return 447.6+(9.2*peso)+(3.1*altura)(4.3*idade)

taxa=taxa.lower()
fator=taxa.replace("í","i")
fator=fator.replace("é","e")
sexo=sexo.lower()
if sexo=="M":                #calcula os valores teoricos para homens
    FuncaoHomem(peso, altura, idade)
    if fator=="minimo":
        TMB=FuncaoHomem*1.2
    if fator=="baixo":
        TMB=FuncaoHomem*1.375
    if fator=="medio":
        TMB=FuncaoHomem*1.55
    if fator=="alto":
        TMB=FuncaoHomem*1.725
    if fator=="muito alto":
        TMB=FuncaoHomem*1.9
        
if sexo="F":                #calcula os valores teoricos para mulheres
    FuncaoMulher(peso, altura, idade)
    if fator=="minimo":
        TMB=FuncaoMulher*1.2
    if fator=="baixo":
        TMB=FuncaoMulher*1.375
    if fator=="medio":
        TMB=FuncaoMulher*1.55
    if fator=="alto":
        TMB=FuncaoMulher*1.725
    if fator=="muito alto":
        TMB=FuncaoMulher*1.9
        
dias=[0]*7
dias[0]=
dias[1]=
dias[2]=
dias[3]=
dias[4]=
dias[5]=
dias[6]=

        
alimentacao_total=[0]*7               #lista com as qtdes de calorias a cada dia
alimentacao_total[0]=
alimentacao_total[1]=
alimentacao_total[2]=
alimentacao_total[3]=
alimentacao_total[4]=
alimentacao_total[5]=
alimentacao_total[6]=

plt.plot(dias,alimentacao_total,'b',label='prático')
plt.plot(dias,TMB,'r',label='ideial')
plt.axis([0,dias,0,4000])
plt.ylabel("calorias")
plt.xlabel("dias")
plt.legend(loc='upper right')
plt.show()