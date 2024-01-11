import pandas as pd

df = pd.read_excel('BoxOffice.xlsx')
# print(df)
# df.info()
print(df.groupby('대표국적').count()['영화명'])
# print(df[df['대표국적'] == '영국'])
# print(df.groupby('대표국적').min('순위')['순위'])



