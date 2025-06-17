# import csv
# with open('Corona.csv','w', newline='') as file:
#     writer= csv.writer(file)
#     writer.writerow(['Country', 'Date', 'New cases', 'Deaths', 'Recovered'])
#     writer.writerow(['India', '2020-01-30', 150, 5, 200])
#     writer.writerow(['USA', '2020-01-31', 120, 10, 100])
#     writer.writerow(['Italy', '2020-01-3', 100, 20, 190])
#     writer.writerow(['China', '2020-01-01', 200, 90, 500])
#     writer.writerow(['Spain', '2020-02-27', 140, 40, 680])
#     writer.writerow(['Germany', '2020-01-29', 160, 50, 300]) 
#     with open('Corona.csv', 'r') as file:
#         reader = csv.reader(file)
# import pandas as pd
# import numpy as np
# df=pd.read_csv('Corona.csv')
# print(df)
# df['Active cases']= df['New cases']- df['Recovered']
# conditions= [
#     (df['Active cases'] < 100),
#     (df['Active cases'] >= 100) & (df['Active cases'] < 500),
#     (df['Active cases'] >= 500)
# ]
# choices= ['High Risk', 'Medium Risk', 'Low Risk']
# df['Risk_level']= np.select(conditions, choices, default= 'Unknown')
# region_summary= df.groupby('Country')[['New cases', 'Deaths', 'Recovered', 'Active cases']].sum()
# print(region_summary)
# import matplotlib.pyplot as plt
# region_summary.plot(kind='bar',title='Corona Virus Summary by Country')

# totals= region_summary.loc['India']
# plt.pie([totals['Deaths'], totals['Recovered'], totals['Active cases']],
#         labels=['Deaths', 'Recovered', 'Active'])
# plt.title('Corona Virus Summary for India')
# plt.show()

import csv
with open('Product.csv','w', newline='') as file:
    writer =csv.writer(file)
    writer.writerow(['Product','Category','Price','Units sold','Ratings','Returns'])
    writer.writerow(['Laptop','Electronics',80000,50,4.5,2])
    writer.writerow(['Mobile','Electronics',30000,100,4.2,5])
    writer.writerow(['Shirt','Clothing',1500,200,4.0,10])
    writer.writerow(['Shoes','Footwear',2500,150,4.3,8])
    writer.writerow(['Watch','Accessories',5000,80,4.1,3])
with open('Product.csv', 'r') as file:
    reader = csv.reader(file)
import pandas as pd
import numpy as np
df = pd.read_csv('Product.csv')


df['Revenue']= df['Price'] * df['Units sold']
df['Return rate%']= (df['Returns'] / df['Units sold']) * 100

conditions = [
    (df['Ratings']>=4.5),
    (df['Ratings']>=4.0) & (df['Ratings']<4.5),
    (df['Ratings']<4.0)
]
choices= ['Excellent', 'Good', 'Average']
df['Rating Category'] = np.select(conditions, choices, default='Unknown')
print(df)
import matplotlib.pyplot as plt
category_revenue = df.groupby('Category')['Revenue'].sum()
plt.pie(category_revenue, labels=category_revenue.index, autopct='%1.1f%%')
plt.title('Revenue by Category')
plt.show()

top5= df.sort_values(by='Revenue', ascending=False).head(5)
plt.bar(top5['Product'], top5['Revenue'])
plt.title('Top 5 Products by Revenue')
plt.show()