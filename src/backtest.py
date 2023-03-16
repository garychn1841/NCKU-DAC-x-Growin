import pandas as pd
import datetime
import math
from pandarallel import pandarallel
import warnings
warnings.filterwarnings("ignore")

pandarallel.initialize(progress_bar = True)



def lnreturn(season, period=10, group = [0,1,2,3,4,5]):

    def cal_return(season='20200331',ticker = 'A',period=3):
        import pandas as pd
        import datetime
        import math
        df =pd.read_csv('data/%s.csv'%(ticker))
        df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
        df.set_index('Date',inplace=True)

        start = [(datetime.date(int(season[:4]),int(season[4:6])+i,int(season[6:])-1).isoformat()[:7])+'-*' for i in range(1,4)]
        df1 = df.filter(regex=start[0],axis=0)
        df2 = df.filter(regex=start[1],axis=0)
        df3 = df.filter(regex=start[2],axis=0)
        df = pd.concat([df1,df2,df3])

        df1 = df.iloc[45:]
        df1['Adj Close'] = df1['Adj Close'].map(lambda x: math.log(x)).diff()
        R = df1['Adj Close'].iloc[1:period].sum()
        # print(df1)
        # print(R)
        return R

    df=pd.read_csv('./clusting_data/%s.csv'%(season))
    df.rename(columns={"Unnamed: 0": "ticker"},inplace=True)
    df = df[df['label'].isin(group)]

    df['return']= df['ticker'].parallel_map(lambda x:cal_return(season,x,period))
    final_df = df[['ticker','label','return']]
    return final_df



if __name__ == '__main__':
    print(lnreturn('20200331',10,[0,2,4]))
    # cal_return(ticker = 'AAPL',period=4)