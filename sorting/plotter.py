import matplotlib.pyplot as plt
import csv
import pandas as pd
import numpy as np

def plot(file='mergesort_test_10.csv'):
    df = pd.read_csv('mergesort_test_10.csv',sep=',')
    
    x = df['items'].to_numpy()
    y = df['time'].to_numpy()

    plt.scatter(x,y,marker='.',s=1)

    # plt.scatter(x2,y2,marker='.',s=1,c='#32a852')

    plt.xlabel('Number of items in list')
    plt.ylabel('Time to sort (s)')
    plt.title('Time taken to sort different sized lists with mergesort')
    plt.show()