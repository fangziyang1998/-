import matplotlib.pyplot as plt
import pandas  as pd
import  numpy as np

plt.rcParams['font.sans-serif'] = 'KaiTi' # Установите глобальный шрифт на китайский курсив
plt.rcParams['axes.unicode_minus'] = False # Не используйте китайский знак минус

#читать данные
data=pd.read_csv("employeeincome.csv")
print (list(data.employee))#преобразовать в список
logy = list(np.log10(data.income))#Возьмем ось Y как логарифм дохода
#colors = np.random.rand(len(list(data.employee)))#Случайный цвет в зависимости от сотрудника
cm = plt.cm.get_cmap('RdYlBu')#Использование хроматограммы RdYlBu 
plt.scatter(list(data.employee), logy,s=100,marker='*')#Постройте точечную диаграмму без использования цвета
plt.xlabel("employee")#Добавить описание оси X
plt.ylabel("imcome")#Добавить описание оси Y
plt.show() 

