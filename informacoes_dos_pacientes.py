# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 19:03:44 2015

@author: Riccardo
"""

from alimentos import alimentos_
from alimentos import alimentos_proteinas
from alimentos import alimentos_carboidratos
from alimentos import alimentos_gordura
from alimentos import proteinas
from alimentos import carboidratos
from alimentos import gordura

informacoes_dos_pacientes= open("usuario.csv.csv","r")
leitura=informacoes_dos_pacientes.readlines()


def CalculaTaxaMetabolismoBasal(peso,altura,idade):
    TMB= 88.36+(13.4*peso)+(4.8*altura)-(5.7*idade)
    return TMB

def CalculaTMBmultAF():
    taoccd=CalculaTaxaMetabolismoBasal(peso,altura,idade)*1.725
    return taoccd

def ReturnPeso():
    Peso = peso
    return Peso
    
def ReturnAltura2():
    Altura2 = altura**2
    return Altura2
    

def CalculaBMI(ReturnPeso,ReturnAltura2):
    BMI=(ReturnPeso())/(ReturnAltura2())  
    return BMI

def change_float_CalculaBMI_to_str():
    change1=(CalculaBMI(ReturnPeso,ReturnAltura2))//1
    changed=str(change1)
    return changed

def ReturnTypeBMI():
    if CalculaBMI(ReturnPeso,ReturnAltura2)<18.5:
        return("Você está com um peso abaixo do normal")
    elif 18.5<=CalculaBMI(ReturnPeso,ReturnAltura2)<25:
        return("Você tem um peso considerado normal")
    elif 25<=CalculaBMI(ReturnPeso,ReturnAltura2)<30:
        return("Você esta levemente acima do peso")
    else:
        return("Você esta com um peso muito acima do normal")
 
UserFoodGramsWeek={}
UserDayCaloriesWeek={}
UserDayProteinsWeek={}
UserDayCarboidratesWeek={}
UserDayFatWeek={}

userpeaces = leitura[1].split(",")
nome = userpeaces[0]
idade = int(userpeaces[1])
peso = float(userpeaces[2])
sexo = userpeaces[3]
altura = float(userpeaces[4])
fator = userpeaces[5]

InformacoesNutricionaisCalPorGrama=alimentos_()
InformacoesNutricionaisProteinasPorGrama=alimentos_proteinas()
InformacoesNutricionaisCarboidratosPorGrama=alimentos_carboidratos()
InformacoesNutricionaisGorduraPorGrama=alimentos_gordura()

def usuariocarboidratos():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        gramas=usergramsamount
        date=userpeaces[0]
           
        if date in UserDayCarboidratesWeek:
            UserDayCarboidratesWeek[date]+=InformacoesNutricionaisCarboidratosPorGrama[food]*gramas
        else:
            UserDayCarboidratesWeek[date]=InformacoesNutricionaisCarboidratosPorGrama[food]*gramas
    
usuariocarboidratos()

def usuariocalorias():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        gramas=usergramsamount
        date=userpeaces[0]
        if date in UserDayCaloriesWeek:
            UserDayCaloriesWeek[date]+=InformacoesNutricionaisCalPorGrama[food]*gramas
        else:
            UserDayCaloriesWeek[date]=InformacoesNutricionaisCalPorGrama[food]*gramas
    
usuariocalorias()

def usuarioproteinas():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        gramas=usergramsamount
        date=userpeaces[0]
        if date in UserDayProteinsWeek:
            UserDayProteinsWeek[date]+=InformacoesNutricionaisProteinasPorGrama[food]*gramas
        else:
            UserDayProteinsWeek[date]=InformacoesNutricionaisProteinasPorGrama[food]*gramas  
   
usuarioproteinas()

def usuariogordura():
    x=0
    for linha in leitura[3:]:
        x+=1
        userpeaces = linha.strip().split(',')
        usergramsamount=float(userpeaces[2])
        food=userpeaces[1]
        gramas=usergramsamount
        date=userpeaces[0]     
        if date in UserDayFatWeek:
            UserDayFatWeek[date]+=InformacoesNutricionaisGorduraPorGrama[food]*gramas
        else:
            UserDayFatWeek[date]=InformacoesNutricionaisGorduraPorGrama[food]*gramas  
    
usuariogordura()
