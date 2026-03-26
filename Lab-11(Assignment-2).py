import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Company': ['Microsoft','Google','Amazon','IBM','Deloitte','Capgemini','ATOS','Amdocs'],
    'Recruitment': [120,150,180,90,110,130,80,95]
}

df = pd.DataFrame(data)

plt.bar(df['Company'], df['Recruitment'])
plt.xticks(rotation=45)
plt.show()

plt.pie(df['Recruitment'], labels=df['Company'], autopct='%1.1f%%')
plt.show()

explode = [0,0,0.1,0,0,0,0,0]
plt.pie(df['Recruitment'], labels=df['Company'], explode=explode, autopct='%1.1f%%')
plt.show()

plt.pie(df['Recruitment'], labels=df['Company'], wedgeprops=dict(width=0.4))
plt.show()

compare = df[df['Company'].isin(['IBM','Amdocs'])]
plt.bar(compare['Company'], compare['Recruitment'])
plt.show()
