import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)


df = pd.read_excel('Life Expectancy Data.xlsx')

shape = df.shape
head = df.head()
tail = df.tail()
types = df.dtypes

# brand new datadrame not to reference o the old one
df = df.drop(['Thinness  1-19 years','Total expenditure','Percentage expenditure','Income composition of resources', ' Thinness 5-9 years','Hepatitis B', 'Polio', ' HIV/AIDS'], axis=1).copy()

#rename columns

df = df.rename(columns={'Infant deaths': 'Deaths'})

# print(df.isna().sum())
# print(df.duplicated())

# checking for duplicates
print(df.duplicated(subset={'Life expectancy ', 'Adult Mortality',
       'Deaths', 'Alcohol',}))

# 3) feature understanding Historgram, KDE, Boxplot

ax = df['Alcohol'].head(10).plot(kind='bar', title='Top Years Drinking Alcohol')
ax.set_xlabel('Countrys')
ax.set_ylabel('alcohol')
plt.show()

plot = df['Deaths'].head(10).plot(kind='hist', bins=20)
plt.show()

#4) feature relationships Scattreplot, Heatmap Correlatio, Pairplot

df.plot(kind='scatter', x='BMI', y='Year', title='Title')
plt.show()

sns.scatterplot(x='Life expectancy ', y='BMI', hue='Year',data=df)
plt.show()
