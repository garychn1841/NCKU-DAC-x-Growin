import pandas as pd
import datetime
import math
import numpy as np
from pandarallel import pandarallel
import warnings
warnings.filterwarnings("ignore")
import yfinance as yf

pandarallel.initialize(progress_bar = True)


# def cal_return(season='20200331',ticker = 'A',period=3):
#     import pandas as pd
#     import datetime
#     import math
#     df =pd.read_csv('data/%s.csv'%(ticker))
#     df['Date'] = pd.to_datetime(df['Date'], format="%Y/%m/%d")
#     df.set_index('Date',inplace=True)

#     start = [(datetime.date(int(season[:4]),int(season[4:6])+i,int(season[6:])-1).isoformat()[:7])+'-*' for i in range(1,4)]
#     df1 = df.filter(regex=start[0],axis=0)
#     df2 = df.filter(regex=start[1],axis=0)
#     df3 = df.filter(regex=start[2],axis=0)
#     df = pd.concat([df1,df2,df3])

#     df1 = df.iloc[45:]
#     R = df1['Adj Close'].map(lambda x: math.log(x))
#     # R = df1['Adj Close'].iloc[1:period].sum()
#     # print(df1)
#     # print(R)
#     return R


def lnreturn(season, period=10, group = [0,1,2,3,4,5]):


    def cal_return(season='20200331',ticker = 'A'):
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
        R = df1['Adj Close'].map(lambda x: math.log(x))
        # R = df1['Adj Close'].iloc[1:period].sum()
        # print(df1)
        # print(R)
        return R

    df=pd.read_csv('./clusting_data/%s.csv'%(season))
    df.rename(columns={"Unnamed: 0": "ticker"},inplace=True)
    df = df[df['label'].isin(group)]

    df['return']= df['ticker'].parallel_map(lambda x:cal_return(season,x).diff().iloc[1:period].sum())
    final_df = df[['ticker','label','return']]
    return final_df

def lnstd(season, period=10, group = [0,1,2,3,4,5]):


    def cal_return(season='20200331',ticker = 'A'):
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
        R = df1['Adj Close'].map(lambda x: math.log(x))

        return R

    df=pd.read_csv('./clusting_data/%s.csv'%(season))
    df.rename(columns={"Unnamed: 0": "ticker"},inplace=True)
    df = df[df['label'].isin(group)]

    df['std']= df['ticker'].parallel_map(lambda x:cal_return(season,x).iloc[:period].std())
    final_df = df[['ticker','label','std']]
    return final_df


def sector(season,group = [0,1,2,3,4,5]):



    df=pd.read_csv('./clusting_data/%s.csv'%(season))
    df.rename(columns={"Unnamed: 0": "ticker"},inplace=True)
    df = df[df['label'].isin(group)]
    df = df[['ticker','label']]

    row_data =pd.read_csv('D:/PYTHON/NCKU-DAC-x-Growin/src/row_data.csv')
    tickermapsector = row_data[['ticker','sector']].drop_duplicates().set_index('ticker')

    df['sector'] = df['ticker'].map(lambda x:(tickermapsector.loc[x].values)[0])
    df2 = df.groupby(['label','sector'])['ticker'].count()
    return df2



def sharperatio(season, period=10, group = [0,1,2,3,4,5]):
    def cal_return(season='20200331',ticker = 'A'):
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
        R = df1['Adj Close'].map(lambda x: math.log(x))

        return R
    

    def rf_date(season='20200331',ticker = 'AAPL',period=10):
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

        rf_date = [list(df1.index)[period].isoformat()[:10],list(df1.index)[period+1].isoformat()[:10]]

        return rf_date
    

    df=pd.read_csv('./clusting_data/%s.csv'%(season))
    df.rename(columns={"Unnamed: 0": "ticker"},inplace=True)
    df = df[df['label'].isin(group)]



    df['return']= df['ticker'].parallel_map(lambda x:cal_return(season,x).diff().iloc[1:period].sum())
    df['std']= df['ticker'].parallel_map(lambda x:cal_return(season,x).iloc[:period].std())

    date = rf_date(season,period=period)
    rf_df = yf.download('^TNX',start = date[0] , end =date[1])
    rf = (rf_df['Adj Close'].values)[0]
    df['sharpe ratio'] = (df['return'] - rf/100)/df['std'] 


    final_df = df[['ticker','label','return','std','sharpe ratio']]
    return final_df


if __name__ == '__main__':
    # print(lnreturn('20200331',10,[0,2,4]))
    # print(lnstd('20200331',10,[0,2,4]))
    # print(sector('20201231',[0,2,4,5]))
    # cal_return(ticker = 'AAPL',period=4)
    print(sharperatio('20220630',15,[0]).head(50))