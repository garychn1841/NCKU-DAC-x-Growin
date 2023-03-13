import pandas as pd 
import matplotlib.pyplot as plt
import talib as ta
from datetime import datetime,timedelta
import yfinance as stock
import numpy as np

# seasonzier
# sensonzier(df = the row data ,investor = which investor is checked):
# output list contain total 12 season data(2d list)
def sensonzier(df,investor):
    df = df[df['investor'] == investor]
    df.sort_values('date')
    df_1 = df[df['date'] == "2020-03-31"]
    df_2 = df[df['date'] == "2020-06-30"]
    df_3 = df[df['date'] == "2020-09-30"]
    df_4 = df[df['date'] == "2020-12-31"]
    df_5 = df[df['date'] == "2021-03-31"]
    df_6 = df[df['date'] == "2021-06-30"]
    df_7 = df[df['date'] == "2021-09-30"]
    df_8 = df[df['date'] == "2021-12-31"]
    df_9 = df[df['date'] == "2022-03-31"]
    df_10 = df[df['date'] == "2022-06-30"]
    df_11 = df[df['date'] == "2022-09-30"]
    df_12 = df[df['date'] == "2022-12-31"]

    return df_1,df_2,df_3,df_4,df_5,df_6,df_7,df_8,df_9,df_10,df_11,df_12


# filtering the new tickers are added in the portfolio
# new_tickers(season_tickers = [a seasonlizer data list]) 
# output list contain the new tickers are added in portfolio for individually 11 season  
def new_tickers(season_tickers):
    x1 = [x for x in season_tickers[1].ticker if x not in season_tickers[0].ticker.values]
    x2 = [x for x in season_tickers[2].ticker if x not in season_tickers[1].ticker.values]
    x3 = [x for x in season_tickers[3].ticker if x not in season_tickers[2].ticker.values]
    x4 = [x for x in season_tickers[4].ticker if x not in season_tickers[3].ticker.values]
    x5 = [x for x in season_tickers[5].ticker if x not in season_tickers[4].ticker.values]
    x6 = [x for x in season_tickers[6].ticker if x not in season_tickers[5].ticker.values]
    x7 = [x for x in season_tickers[7].ticker if x not in season_tickers[6].ticker.values]
    x8 = [x for x in season_tickers[8].ticker if x not in season_tickers[7].ticker.values]
    x9 = [x for x in season_tickers[9].ticker if x not in season_tickers[8].ticker.values]
    x10 = [x for x in season_tickers[10].ticker if x not in season_tickers[9].ticker.values]
    x11 = [x for x in season_tickers[11].ticker if x not in season_tickers[10].ticker.values]

    return x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11

# computing the average wave for the next 15 days
# price(ticker = the list of new tickers are add for indivdually season)
# output the average wave 

def price(ticker,date,investor,phase,index):

    tol = 0
    ave = 0
    count = 0
    
    
    if ticker:
        for i in range(len(ticker)):
            start = date + timedelta(days=45)
            end = start + timedelta(days=15)
            a = stock.download(str(ticker[i]),start=start,end=end)

            min = a['Adj Close'].min()
            max = a['Adj Close'].max()

            if not a.empty:
                tol = tol + (max-min)/min 
                count = count + 1
                print(print(investor,ticker[i],phase,index,'%d/%d'%(count,len(ticker))))
            # aa.append(ticker[i]) if ((max-min)/min) >= 0.10 else None
        #     print(str(ticker[i]))
        #     print("accumulated:",tol)

        # print(ticker , len(ticker))＄Ｓ
        ave = tol / count

    return ave

def same_tickers(season_tickers):


    x1 = [x for x in season_tickers[1].ticker if x in season_tickers[0].ticker.values and season_tickers[0][season_tickers[0]['ticker'] == x].head(1).shares.values == season_tickers[1][season_tickers[1]['ticker'] == x].head(1).shares.values]
    x2 = [x for x in season_tickers[2].ticker if x in season_tickers[1].ticker.values and season_tickers[2][season_tickers[2]['ticker'] == x].head(1).shares.values == season_tickers[1][season_tickers[1]['ticker'] == x].head(1).shares.values] 
    x3 = [x for x in season_tickers[3].ticker if x in season_tickers[2].ticker.values and season_tickers[3][season_tickers[3]['ticker'] == x].head(1).shares.values == season_tickers[2][season_tickers[2]['ticker'] == x].head(1).shares.values]
    x4 = [x for x in season_tickers[4].ticker if x in season_tickers[3].ticker.values and season_tickers[4][season_tickers[4]['ticker'] == x].head(1).shares.values == season_tickers[3][season_tickers[3]['ticker'] == x].head(1).shares.values]
    x5 = [x for x in season_tickers[5].ticker if x in season_tickers[4].ticker.values and season_tickers[5][season_tickers[5]['ticker'] == x].head(1).shares.values == season_tickers[4][season_tickers[4]['ticker'] == x].head(1).shares.values]
    x6 = [x for x in season_tickers[6].ticker if x in season_tickers[5].ticker.values and season_tickers[6][season_tickers[6]['ticker'] == x].head(1).shares.values == season_tickers[5][season_tickers[5]['ticker'] == x].head(1).shares.values]
    x7 = [x for x in season_tickers[7].ticker if x in season_tickers[6].ticker.values and season_tickers[7][season_tickers[7]['ticker'] == x].head(1).shares.values == season_tickers[6][season_tickers[6]['ticker'] == x].head(1).shares.values]
    x8 = [x for x in season_tickers[8].ticker if x in season_tickers[7].ticker.values and season_tickers[8][season_tickers[8]['ticker'] == x].head(1).shares.values == season_tickers[7][season_tickers[7]['ticker'] == x].head(1).shares.values]
    x9 = [x for x in season_tickers[9].ticker if x in season_tickers[8].ticker.values and season_tickers[9][season_tickers[9]['ticker'] == x].head(1).shares.values == season_tickers[8][season_tickers[8]['ticker'] == x].head(1).shares.values]
    x10 = [x for x in season_tickers[10].ticker if x in season_tickers[9].ticker.values and season_tickers[10][season_tickers[10]['ticker'] == x].head(1).shares.values == season_tickers[9][season_tickers[9]['ticker'] == x].head(1).shares.values]
    x11 = [x for x in season_tickers[11].ticker if x in season_tickers[10].ticker.values and season_tickers[11][season_tickers[11]['ticker'] == x].head(1).shares.values == season_tickers[10][season_tickers[10]['ticker'] == x].head(1).shares.values]

    return x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11


# a = stock.download('BF.B',start='2023-01-01',end='2023-01-20')
# print(a)

if __name__ == '__main__':

    better_10 = []
    average_percent = []
    ave_plt = []
    average_dict = {}

    df = pd.read_csv('/Users/gary/Documents/Python/data/growin/row_data.csv')
    df = df[df['style']=='Hedge Fund']
    df = df.drop(df[df['ticker'] == 'GTLS PR B'].index)
    df = df.drop(df[df['ticker'] == 'S'].index)
    # unchangelist(df)

    season = df.date.unique()
    season = [datetime.strptime(x,'%Y-%m-%d') for x in season]
    investor = df.investor.unique()
     
    print(investor)

    # a = stock.download('GTLS PR B',start='2023-01-01',end='2023-03-04')
    # print(a)
    for name in investor[3:5]:
    
        df_season = sensonzier(df,name)
        new_ticker_list = new_tickers(df_season)
        same = same_tickers(df_season)

        tol_ave = 0 
        tol_ave_same = 0


        for index,element in enumerate(new_ticker_list):
            ave = price(element,season[1+index],name,"new",index)
            tol_ave = tol_ave + ave
            ave_plt.append(ave)

        for index,element in enumerate(same):
            same_ave = price(element,season[1+index],name,'same',index)
            tol_ave_same = tol_ave + same_ave
            ave_plt.append(same_ave)

        tol_average = tol_ave/len(new_ticker_list)
        same_average = tol_ave_same/len(same)
        y = (tol_average,same_average)
        average_dict = {name : y}
 
    print(average_dict)


    # x = np.arange(1,12)
    # plt.bar(x,ave_plt)
    # plt.xlabel('season')
    # plt.ylabel('percentage of wave')
    # plt.savefig('plot.png')
    # plt.show()