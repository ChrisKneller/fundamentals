import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np
from itertools import cycle
from performance import sorting_algorithms

def plot(file='csv/sorting_comparison.csv'):

    cycol = cycle('bgrcmk')

    df = pd.read_csv(file,sep=',')

    for i,algorithm in enumerate(sorting_algorithms):
        df1 = df.loc[df['algorithm'] == algorithm]

        x = df1['num_items'].to_numpy()
        y = df1['time(s)'].to_numpy()

        plt.scatter(x,y,marker='.',c=next(cycol),s=1,label=algorithm)

    plt.xlabel('Number of items in list')
    plt.ylabel('Time to sort (s)')
    plt.title('Time taken to sort different sized lists with different algorithms')
    plt.legend()
    plt.savefig('plots/all.png')