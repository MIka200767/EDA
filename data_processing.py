import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns


df = pd.read_excel('Life Expectancy Data.xlsx')
 
#finding missing values, ducplicates, garbage values

print(df.isnull().sum())

print(df.duplicated().sum())

for i in df.select_dtypes(include='object').columns:
    print(df[i].value_counts())

# EDA
#descriptive statistics

# print(df.describe().T)

#histogram undestand the distribution

for i in df.select_dtypes(include='number').columns:
    sns.histplot(data=df, x=i)
    plt.show()

#scatter plott to understand the relationship (life expectancy) 

for i in ['Year', 'Adult Mortality', 'Infant deaths', 'Alcohol','Percentage expenditure', 'Hepatitis B', 'Measles ', 'BMI', 'Under-five deaths','Polio', 'Total expenditure', 'Diphteria', 'HIV/AIDS', 'GDP', 'Population','Thinness 1-19 years', 'Thinnes 5-9 years', 'Income composition of resources', 'Schooling']:
    sns.scatterplot(data=df, x=i, y='Life expectancy ')
    plt.show()

# correlation with heatmap to interpret the relation and multicolliniarity

plt.figure(figsize=(15, 15))
numeric_df = df.select_dtypes(include='number').corr()
s = sns.heatmap(numeric_df, annot=True)
print(plt.show())

#misiing values treatments
#choose the method of imputing missing value like  
# continious data=mean, median || discrete, categorical variable=mode

for i in ['BMI', 'Polio', 'Income composition of resources']:
    df[i].fillna(df[i].median(), inplace=True)

print(df.isnull().sum())

#outliers treatments
for i in ['GDP']:
    df[i]=df[i].fillna(df[i].mean())


def wisker(col):
    q1,q3 = np.percentile(col,[25,75])
    iqr=q3-q1
    lw=q1-1.5*iqr 
    up=q3+1.5*iqr
    return lw, up

for i in ['GDP', 'Total expenditure', 'Thinness  1-19 years']:
    lw,up=wisker(df[i])
    df[i]=np.where(df[i]<lw,lw,df[i])
    df[i]=np.where(df[i]>up,up,df[i])

def run():
    for i in ['GDP', 'Total expenditure', 'Thinness  1-19 years']:
        sns.boxplot(df[i])
        plt.show()

run()

#duplicates and garbage value treatments
# df.drop_duplicates()


#encoding of data (convert object data into numeric)

dummies = pd.get_dummies(data=df, columns=['Country', 'Status'], drop_first=True)
print(dummies)