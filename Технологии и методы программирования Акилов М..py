#Написать программу вывода графиков со сканированием точек

import os
import matplotlib.pyplot as plt
from math import sin, cos, tan, sqrt, fabs
import numpy as np

#Функция решаемой функции, входной параметр x.
def function(x,s):
    function = eval(s)
    return function
    
#Ввод значений x.
def inx():
    #Ввод с границами и интервалом.
    x_values = []
    nleft = input("Введите левую границу  x\n")
    nright = input("Введите правую границу x\n")
    nstep = input("Введите интервал x\n")
    x_values = list(np.arange(float(nleft), float(nright),float(nstep)))

    #Возвращаем все значения введеных x в списке.
    return x_values

#Функция создающая список с ответами для каждого x. 
def answ(x_values,s):
    f =[(function(x,s)) for x in x_values]
    #Возвращаем список всех ответов f(x) в списке.
    return f
    
#Создание графика.
def graph(x_values,f,s):
    y_values = [(function(x,s)) for x in x_values]
    plt.plot(x_values, y_values)
    #Для каждого значения ставим метку с координатами.
    for x in x_values:
        y_values = function(x,s)
        plt.annotate('(' + str(x)[:4] + ":" + str(y_values)[:4] + ")",
        xy = (x,y_values), fontsize=4)
    #Название.
    plt.title(s, fontsize=24)
    plt.xlabel("x", fontsize=11)
    plt.ylabel("y", fontsize=11)
    #Границы осей.
    plt.axis([min(x_values),max(x_values) , min(f), max(f)])
    #Вывод графика.
    plt.show()
    
# Основной цикл.
while True:
    key = input("Выберите режим сканирования графика:\n Aвтоматическое-1\n Pучное-2 \n")
    if key == '2':
       
        x_values = inx()
        s = input("Введите формулу\n")
        try:
            #Вызываем функцию, для решения функции.
            f = answ(x_values,s)
            print("Сканирование завершено,см.график")
        except NameError:
            print("Неверно введены значения x")
        try:
            #Выводим график значений.
            graph(x_values,f,s)
        except NameError:
            print("Функция не считается")
    elif key == '1':
        x_values = []
        nleft = input("Введите левую границу  x\n")
        nright = input("Введите правую границу x\n")
        x_values = list(np.arange(float(nleft), float(nright),0.5))
        s = input("Введите формулу\n")
        f = answ(x_values,s)
        graph(x_values,f,s)
        

    if input("Завершить работу?(y/n)") == 'y':
        break
    


