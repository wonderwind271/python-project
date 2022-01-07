import pandas as pd
import numpy as np

def row_insert(df, i, df_add):
    # 指定第i行插入一行数据
    df1 = df.iloc[:i, :]
    df2 = df.iloc[i:, :]
    df_new = pd.concat([df1, df_add, df2], ignore_index=True)
    return df_new



records=pd.read_csv('account.csv',names=['item','price','date','method','note'])
# print(records.loc[0])
records_data=np.array(records)
# print(records_data)

print("successfully read data, please input commands. Input help to get a manual for the commands")

help_list=[]
cmd=""
print(records)

while cmd!='q':
    cmd=input("> ")
    # start processing
    if cmd=='help':
        print(help_list)
    elif cmd=='l' or cmd=='list':
        print(records.to_string())
    elif cmd=='add':
        print('creating new record...')



