# -*- coding: utf-8 -*-
# Author: AdilsonLNCrist
# Date: 02/07/2019

import matplotlib.pyplot as plt

dados = open("ticket.csv").readlines()

#Títulos
title = "Gráfico de variação de ações mês de Junho/2019"
eixox = "Dias do mês de junho"
eixoy = "Valor/R$"
# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)
#Variaveis
x = []
petr = []
itub = []
bbdc = []
ggbr = []
itsa = []
# Codigo
for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append((linha[0]))
        petr.append(float(linha[1]))
        itub.append(float(linha[3]))
        bbdc.append(float(linha[5]))
        ggbr.append(float(linha[7]))
        itsa.append(float(linha[9]))
plt.scatter(x, petr, color="k")
plt.scatter(x, itub, color="k")
plt.scatter(x, bbdc, color="k")
plt.scatter(x, ggbr, color="k")
plt.scatter(x, itsa, color="k")
plt.scatter(x, petr, label="PETR4", color="k", marker=".")
plt.scatter(x, itub, label="ITUB4", color="y", marker=".")
plt.scatter(x, bbdc, label="BBDC4", color="r", marker=".")
plt.scatter(x, ggbr, label="GGBR4", color="b", marker=".")
plt.scatter(x, itsa, label="ITSA4", color="m", marker=".")
plt.legend(bbox_to_anchor=(0.93,0.93), loc='upper left')
plt.show()
