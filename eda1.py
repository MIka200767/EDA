import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.style.use('ggplot')
pd.set_option('display.max_columns', 200)


df = pd.read_csv('climate_change_impact_on_agriculture_2024.csv', )
df = df.drop(['Adaptation_Strategies', 'Crop_Yield_MT_per_HA', 'Economic_Impact_Million_USD'], axis=1 ).copy()

# 1) sanity check

duplicated = df.duplicated().sum()
na = df.isna().sum()

# 2) EDA descriptive statistics
print(df.describe().T)
#histogram 

for i in df.select_dtypes(include='number').columns:
    sns.histplot(data=df, x=i)
    plt.show()

#boxplot to determine outliers

for i in df.select_dtypes(include='number').columns:
    sns.boxplot(data=df, x=i)
    plt.show()

#scatterplot to understand relationship

for i in ['Country', 'Region', 'Crop_Type', 'Average_Temperature_C', 'CO2_Emissions_MT', 'Extreme_Weather_Events',
       'Irrigation_Access_%', 'Pesticide_Use_KG_per_HA',
       'Fertilizer_Use_KG_per_HA', 'Soil_Health_Index']:
    sns.scatterplot(data=df, x=i, y='Total_Precipitation_mm')
    plt.show()

#small correlation based on heatmap

plt.figure(figsize=(15, 15))
numeric_df = df.select_dtypes(include='number').corr()
s = sns.heatmap(numeric_df, annot=True)
print(plt.show())

# missing value treatmens

for i in ['Country', 'Region', 'Crop_Type', 'Average_Temperature_C', 'CO2_Emissions_MT', 'Extreme_Weather_Events', 'Irrigation_Access_%', 'Pesticide_Use_KG_per_HA',
    'Fertilizer_Use_KG_per_HA', 'Soil_Health_Index']:
    df[i] = df[i].fillna(df[i].median())

#outliers

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