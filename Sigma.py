import h5py
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def dataReadPanda():
    data = pd.read_hdf('C:/Users/Anurag/PycharmProjects/SigmaProject/train.h5/train.h5')
    print data.head(5)
    return data

def findOutTimeStamps(data):

    colmunDataFrame = data.groupby('id').timestamp.nunique()
    ids = set(data['id'])
    for id in ids:
        seven_data = data[data['id'] == id]
        seven_data[['timestamp', 'y']].sort_values(['timestamp']).plot(x='timestamp', y='y', kind='line')
        saveStr = 'C:/Users/Anurag/PycharmProjects/SigmaProject/data_'.strip() + str(id).strip() + '.png'.strip()
        print saveStr
        plt.savefig(saveStr)
        # plt.show()

    # print seven_data[['timestamp', 'y']].sort_values(['timestamp']).plot(x = 'timestamp', y = 'y', kind='line')

def findCorrelation():
    pass

if __name__ == "__main__":
    data = dataReadPanda()
    findOutTimeStamps(data)
