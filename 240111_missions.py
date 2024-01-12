import matplotlib.pyplot as plt 
import pandas as pd
import numpy as np 
import seaborn as sns 

##### mission1
# x = np.arange(1, 11)
# y = np.random.randint(1, 30, 10)
# plt.scatter(x, y, c='r', marker='s')
# plt.show()


# ##### mission2
# plt.rc('font', family='NanumGothic')
# df = pd.read_excel('data1.xlsx')
# # print(df)
# plt.plot(df['name'], df['kor'], 'go--', label='국어점수')
# plt.plot(df['name'], df['math'], 'r*-', label='수학점수')
# plt.legend()
# plt.title('성적 그래프')
# plt.xlabel('이름')
# plt.ylabel('점수')
# plt.show()


##### mission3
##문제1
# penguins = pd.read_csv('penguins.csv')
# print(penguins)
# print(penguins.columns)
# # penguins.info()
# sns.barplot(x='species', y='body_mass_g', hue='sex', data=penguins, errorbar='sd')
# plt.show()
##문제2
# penguins = pd.read_csv('penguins.csv')
# print(penguins.columns)
# sns.pairplot(penguins, hue='sex')
# plt.show()
##문제3
penguins = pd.read_csv('penguins.csv')
sns.regplot(x='flipper_length_mm', y='body_mass_g', data=penguins)
plt.show()






