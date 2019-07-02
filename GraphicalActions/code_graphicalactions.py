# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt

dados = open("ticket.csv").readlines()

#Variaveis
title = "Gráfico de variação de ações mês de Junho/2019"
eixox = "Dias do mês de junho"
eixoy = "Valor/R$"
# Legendas
plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)


x = []
petr = []
itub = []
bbdc = []
ggbr = []
itsa = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")
        x.append((linha[0]))
        petr.append(float(linha[1]))
        itub.append(float(linha[3]))
        bbdc.append(float(linha[5]))
        ggbr.append(float(linha[7]))
        itsa.append(float(linha[9]))
plt.scatter(x, petr, color="k")#, linestyle=":")
plt.scatter(x, itub, color="k")#, linestyle=":")
plt.scatter(x, bbdc, color="k")#, linestyle=":")
plt.scatter(x, ggbr, color="k")#, linestyle=":")
plt.scatter(x, itsa, color="k")#, linestyle=":")
plt.scatter(x, petr, label="PETR4", color="k", marker=".")
plt.scatter(x, itub, label="ITUB4", color="y", marker=".")
plt.scatter(x, bbdc, label="BBDC4", color="r", marker=".")
plt.scatter(x, ggbr, label="GGBR4", color="b", marker=".")
plt.scatter(x, itsa, label="ITSA4", color="m", marker=".")
plt.legend(bbox_to_anchor=(0.93,0.93), loc='upper left')
#plt.legend()
plt.show()
