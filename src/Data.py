import pandas as pd 
import numpy as np


# investor (str)：金融機構名稱
# ticker (str)：股票代碼
# shares (float)：持有單位數
# value (float)：持有部位
# date (str)：日期

# style (str)：機構風格
# (成長、存股、價值、GARP、避險基金各20間)
# sector (str)：股票版塊
# mkt_cap (float)：市值

def readdata():
    df1 = pd.read_csv('./dataset/[NCKU]13F籌碼面資料_part1.csv',index_col=[0])
    df2 = pd.read_csv('./dataset/[NCKU]13F籌碼面資料_part2.csv',index_col=[0])
    df_all = pd.concat([df1,df2],ignore_index=True)
    df_all.date = df_all.date.map(str)
    df_all.date = pd.to_datetime(df_all.date)
    return df_all

def navalue(df):
    na = df.isnull()
    return np.any(na)


if __name__ == "__main__":
    df_all = readdata()
    print(navalue(df_all))
    df_all.to_csv('row_data.csv',index=False)

