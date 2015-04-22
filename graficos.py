# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 18:41:28 2015

@author: Riccardo
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from informacoes_dos_pacientes import UserDayCaloriesWeek
from informacoes_dos_pacientes import UserDayProteinsWeek
from informacoes_dos_pacientes import UserDayCarboidratesWeek
from informacoes_dos_pacientes import UserDayFatWeek
from informacoes_dos_pacientes import CalculaTMBmultAF
from funcoes import CalculaSumUserDayCaloriesWeek


categoria = ('Calorias consumidas','calorias recomendadas',)
y_pos = np.arange(len(categoria))
quantidade = [CalculaSumUserDayCaloriesWeek(),CalculaTMBmultAF()]
plt.barh(y_pos, quantidade, align='center', alpha=0.4)
plt.yticks(y_pos, categoria)
plt.xlabel('Quantidade (calorias)')
plt.title('Quantidade diaria recomendada vs consumida')
plt.show()

num_dias_cal = len(list(UserDayCaloriesWeek.keys()))
num_dias_proteinas = len(list(UserDayProteinsWeek.keys()))
num_dias_carboidratos = len(list(UserDayCarboidratesWeek.values()))
num_dias_gordura=len(list(UserDayFatWeek.values()))


days=list(UserDayCaloriesWeek.keys())
days.sort()

calorias_valores=[]
for d in days:
    calorias_valores.append(UserDayCaloriesWeek[d])
print(UserDayCaloriesWeek)
print("UserDayCaloriesWeek",days)
print("UserDayCaloriesWeek",calorias_valores)

plt.plot(list(range(num_dias_cal)),calorias_valores)
plt.xlabel("Dias da semana")
plt.ylabel("Calorias")
plt.title("Quantidade de Calorias na semana")
plt.xticks(range(len(days)), days)
plt.show()


proteinas_valores=[]
for d in days:
    proteinas_valores.append(UserDayProteinsWeek[d])
print("UserDayProteinsWeek",UserDayProteinsWeek)
print("UserDayProteinsWeek",days)
print("UserDayProteinsWeek",proteinas_valores)

plt.plot(list(range(num_dias_proteinas)),proteinas_valores)
plt.xlabel("Dias da semana")
plt.ylabel("Proteinas")
plt.title("Quantidade de proteinas na semana")
plt.xticks(range(len(days)), days)
plt.show()


carboidratos_valores=[]
for d in days:
    carboidratos_valores.append(UserDayCarboidratesWeek[d])
print("UserDayCarboidratesWeek",UserDayCarboidratesWeek)
print("UserDayCarboidratesWeek",days)
print("UserDayCarboidratesWeek",carboidratos_valores)


plt.plot(list(range(num_dias_carboidratos)),carboidratos_valores)
plt.xlabel("Dias da semana")
plt.ylabel("Carboidratos")
plt.title("Quantidade de carboidratos ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()


gordura_valores=[]
for d in days:
    gordura_valores.append(UserDayFatWeek[d])
print("UserDayFatWeek",UserDayFatWeek)
print("UserDayFatWeek",days)
print("UserDayFatWeek",gordura_valores)

plt.plot(list(range(num_dias_gordura)),gordura_valores)
plt.xlabel("Dias da semana")
plt.ylabel("Gordura")
plt.title("Quantidade de gordura ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()

plt.plot(list(range(num_dias_cal)),calorias_valores,list(range(num_dias_proteinas)),proteinas_valores,list(range(num_dias_carboidratos)),carboidratos_valores,list(range(num_dias_gordura)),gordura_valores)
plt.xlabel("Dias da semana")
plt.ylabel("Calorias, Proteinas, Carboidratos e Gordura")
plt.title("Quantidade ao longo da semana")
plt.xticks(range(len(days)), days)
plt.show()
