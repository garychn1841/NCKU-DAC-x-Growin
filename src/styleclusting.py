import pandas as pd 
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/gary/Documents/Python/data/growin/styleweight/StyleWeight_full.csv')
season = df['Unnamed: 0.1'].unique()
for i  in range(3,7):
    for period in season:

        df1 = df[df['Unnamed: 0.1'] == period]
        df1 = df1.drop(['Unnamed: 0.1','Unnamed: 1'], axis=1).set_index('Unnamed: 0').T
        df1 = df1[df1.cumsum(axis = 1)['Aggres. Gr.'] != 0.0]
        x = df1.to_numpy()

        kmeans = KMeans(n_clusters=i,random_state=1,n_init="auto").fit(x)
        df1['label'] = kmeans.labels_
        df1.to_csv('%s_n%s.csv'%(period,i),index = False)