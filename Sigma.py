import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def dataReadPanda():
    data = pd.read_hdf('./train.h5/train.h5')
    print data.head(5)
    return data

def findOutTimeStamps(data):
    colmunDataFrame = data.groupby('id').timestamp.nunique()
    ids = set(data['id'])
    for id in ids:
        seven_data = data[data['id'] == id]
        seven_data[['timestamp', 'y']].sort_values(['timestamp']).plot(x='timestamp', y='y', kind='line')
        saveStr = './data/data_'.strip() + str(id).strip() + '.png'.strip()
        print saveStr
        plt.savefig(saveStr)
        # plt.show()
    # print seven_data[['timestamp', 'y']].sort_values(['timestamp']).plot(x = 'timestamp', y = 'y', kind='line')

def get_mean(train):
    means_ = train.mean(axis=0)
    return means_

def findOutColumnsCorrelation(data):
    means_ = get_mean(data)
    data.fillna(means_, inplace=True)
    ids = set(data['id'])
    name_of_col = data.columns
    order_col_id = {}
    for id in ids:
        corDict = {}
        seven_data = data[data['id'] == id]
        y_data = seven_data['y']
        for c in name_of_col:
            corDict[c] = np.corrcoef(y_data, np.array(seven_data[c]))[0, 1]
        corD = sorted(corDict, key=corDict.get, reverse=True)
        order_col_id[id] = corD
    return order_col_id

if __name__ == "__main__":
    data = dataReadPanda()
    # findOutTimeStamps(data)
    findOutColumnsCorrelation(data)
