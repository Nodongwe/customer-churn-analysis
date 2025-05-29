#churn_analysis.py


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Load dataset
df = pd.read_csv('customer_churn.csv')

#check the data
print("First 5 rows of the dataset:")
print(df.head())

#Basic info
print("\nData Types and Missing values:")
print(df['Churn'].value_counts())


#Viz: churn by gender
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='gender', hue='Churn')
plt.title('Customer Churn by Gender')
plt.savefig('churn_by_gender.png')
plt.show()