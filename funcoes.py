# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:38:06 2015

@author: Riccardo
"""

from informacoes_dos_pacientes import UserDayCaloriesWeek
from informacoes_dos_pacientes import UserFoodGramsWeek
from informacoes_dos_pacientes import CalculaTMBmultAF


'''
def CalculaGramsCaloriesGrams(d1, d2):
    d3 = dict()
    for k in d1:
        if k in d2:
            d3[k] = d1[k] * d2[k]
    return d3
'''
def CalculaSumUserDayCaloriesWeek():
    a=(sum(UserDayCaloriesWeek.values())/7)
    return a
    #print("O total de calorias consumidas é de ",a, "calorias por dia.")



def CalculasumgmultcpergsubtraiCalculaTMBmultAF():
    f=(CalculaSumUserDayCaloriesWeek()-CalculaTMBmultAF())
    return f
    
print("O total de calorias recomendadas é de ",CalculaTMBmultAF(), " cal/dia.")
print("O seu balanço calórico diario é de ", CalculasumgmultcpergsubtraiCalculaTMBmultAF()," calorias")
print("O total de calorias consumidas é de ",CalculaSumUserDayCaloriesWeek()," cal/dia.")