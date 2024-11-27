import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)

#sanity check
df = pd.read_csv('iplauction2023.csv')

df = df.rename(columns={'final price (in lacs)': 'final price', 'base price (in lacs)': 'base price'})

print(df.isna().sum())
print('duplicated', df.duplicated().sum())

for i in df.select_dtypes(include='object').columns:
    print(df[i].value_counts())
    print('**************')

mean_baseprice = df['base price'].mean()
mean_baseprice = df['base price'].median()

#EDA descriptive statistics

#histogram to understand distribution

for i in df.select_dtypes(include='numeric').columns:
    sns.histplot(data=df, x=i)
    plt.show()

# boxplot

for i in df.select_dtypes(include='number').columns:
    sns.boxplot(data=df, x=i)
    plt.show()


#scatter plot to understand the relationship

for i in ['final price']:
    sns.scatterplot(data=df, x=i, y='base price')
    plt.show()

#understand correlation with heatmap
sns.heatmap(df.select_dtypes(include='number').corr()) 
plt.show()

#missing value treatments

print(df.isnull().sum())

for i in ['final price']:
    df[i]=df[i].fillna(df[i].median())

print(df['base price'].isnull().sum()) 
print(df['base price'])  

#outlier treatments

def wisker(col):
    q1,q3 = np.percentile(col, [25, 75])
    iqr = q3 - q1
    lw = q1-1.5*iqr
    uw = q3+1.5*iqr
    return lw, uw

for i in ['final price']:
    lw,uw = wisker(df[i])
    df[i]=np.where(df[i]<lw,lw,df[i])
    df[i]=np.where(df[i]>uw,uw,df[i])


for i in ['final price']:
    sns.boxplot(df[i])
    plt.show()

w = wisker(df['final price'])
