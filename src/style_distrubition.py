#%%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('row_data.csv')
df_season = df.groupby(['date','style']).sum()
x_label= df.date.unique()[8:]
print(df_season.head(20))

plt.figure(figsize=(12,9))

# set height of bar
y1,y2,y3,y4,y5,y6 = [],[],[],[],[],[]
for label in x_label:
    y1.append(df_season.loc[(label,'Aggres. Gr.'),'value'])
    y2.append(df_season.loc[(label,'GARP'),'value'])
    y3.append(df_season.loc[(label,'Growth'),'value'])
    y4.append(df_season.loc[(label,'Hedge Fund'),'value'])
    y5.append(df_season.loc[(label,'Income'),'value'])
    y6.append(df_season.loc[(label,'Value'),'value'])

# Set position of bar on X axis
width = 0.1

x_loc1 = np.arange(len(x_label))
x_loc2 = [i + width for i in x_loc1]
x_loc3 = [i + width for i in x_loc2]
x_loc4 = [i + width for i in x_loc3] 
x_loc5 = [i + width for i in x_loc4]
x_loc6 = [i + width for i in x_loc5]

# Make the plot
plt.bar(x_loc1, y1, color ='tab:blue', width = width, edgecolor ='grey', label ='Aggres. Gr.')
plt.bar(x_loc2, y2, color ='tab:orange', width = width, edgecolor ='grey', label ='GARP')
plt.bar(x_loc3, y3, color ='tab:green', width = width, edgecolor ='grey', label ='Growth')
plt.bar(x_loc4, y4, color ='tab:red', width = width, edgecolor ='grey', label ='Hedge Fund')
plt.bar(x_loc5, y5, color ='tab:purple', width = width, edgecolor ='grey', label ='Income')
plt.bar(x_loc6, y6, color ='tab:brown', width = width, edgecolor ='grey', label ='Value')

# Adding Xticks
plt.xlabel('Season', fontweight ='bold', fontsize = 15)
plt.ylabel('goods', fontweight ='bold', fontsize = 15)
plt.xticks([r + width*2+0.05 for r in range(len(y1))],x_label)
 
plt.legend()
plt.show()

#%%
df.date = df.date.to_string()
print(df.head(10))
# df.date = pd.to_datetime(df.date)
# print(df)




# %%
