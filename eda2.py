import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)


df = pd.read_excel('Life Expectancy Data.xlsx')
df = df.drop(['Percentage expenditure', 'Income composition of resources', 'Schooling', ' Thinness 5-9 years', 'Population', 'Total expenditure', 'Under-five deaths '], axis=1).copy()

#sanity check

duplicated = df.duplicated().sum()
na = df.isna().sum()
print(duplicated)
print('*******')
print(na)

# EDA descriptive statistics

print(df.describe().T)

#histogram understand distribution

for i in df.select_dtypes(include='number').columns:
    sns.histplot(data=df, x=i)
    plt.show()

#boxplot

for i in df.select_dtypes(include='number').columns:
    sns.boxplot(data=df, x=i)
    plt.show()

#scatterplot to understand relationship

for i in ['Life expectancy ', 'Adult Mortality',
    'Alcohol', 'Hepatitis B', 'Measles', 'BMI', 'Polio',
    'Diphtheria ', ' HIV/AIDS', 'GDP', 'Thinness  1-19 years']:
    sns.scatterplot(data=df, x=i, y='Infant deaths')
    plt.show()

#heatmap to understand correlation 

plt.figure(figsize=(15, 15))
numeric_df = df.select_dtypes(include='number').corr()
sns.heatmap(numeric_df, annot=True)
plt.show()


#missing value treatments

for i in ['Life expectancy ', 'Adult Mortality',
    'Alcohol', 'Hepatitis B', 'Measles', 'BMI', 'Polio',
    'Diphtheria ', ' HIV/AIDS', 'GDP', 'Thinness  1-19 years']:
    df[i] = df[i].fillna(df[i].median())

#outlier treatments

def wisker(col):
    q1, q3 = np.percentile(col, [25, 75])
    iqr = q3 - q1
    lw = q1-1.5*iqr
    up = q3+1.5*iqr
    return lw, up

for i in ['Life expectancy ', 'Adult Mortality',
    'Alcohol', 'Hepatitis B', 'Measles', 'BMI', 'Polio',
    'Diphtheria ', ' HIV/AIDS', 'GDP', 'Thinness  1-19 years']:
    lw, up = wisker(df[i])
    df[i] = np.where(df[i]<lw,lw,df[i])
    df[i] = np.where(df[i]>up,up,df[i])

def run():
    for i in ['Life expectancy ', 'Adult Mortality',
    'Alcohol', 'Hepatitis B', 'Measles', 'BMI', 'Polio',
    'Diphtheria ', ' HIV/AIDS', 'GDP', 'Thinness  1-19 years']:
        sns.boxplot(x=df[i])
        plt.show()

run()
# print(df.isna().sum())
# print(df.duplicated().sum())

