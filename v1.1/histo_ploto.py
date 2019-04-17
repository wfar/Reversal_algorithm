import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import PercentFormatter


files = ['FP_daf2_3_d17.csv','CM_daf2_3_d17.csv', 'R_n2_3_d1.csv', 'FP_n2_3_d1.csv', 'CM_n2_3_d1.csv',
         'Rrev_new_n2_3_d1_schafer.csv', 'Rrev_new_daf2_3_d17_schafer.csv', 'NRrev_new_n2_3_d1_schafer.csv', 'NRrev_new_daf2_3_d17_schafer.csv',
         'daf2_3_d17_full_data_in_mm.csv', 'n2_3_d1_full_data_in_mm.csv' ]

title = ['Distance for every False Positive in daf2', 'Distance for every Camera Movement in daf2', 'Distance for every Reversal in n2', 'Distance for every False Positive in n2',
         'Distance for every Camera Movement in n2', 'Distance for All reversal detected in n2', 'Distance for All reversal detected in daf2', 'Distance for All non-reversal detected in n2',
         'Distance for All non-reversal detected in daf2', 'Distance for all consecuvtive frames in daf2', 'Distance for all consecuvtive frames in n2']
count = 0
for file in files:
    
    data = pd.read_csv(file, sep=',',header=None)
    dist = data[0]
    x = data[1]
    y = data[2]

    print(title[count])
    print(dist.describe())
    print()


    
    plt.hist(dist, weights=np.zeros_like(dist) + 100. / dist.size, bins = 100)
    #plt.axis([0, 1, 0, 400])

    #plt.axis('tight')
    plt.xlabel('distance (mm)')
    plt.ylabel('Frequency (percentage %)')
    plt.title(title[count])
    #plt.gca().yaxis.set_major_formatter(PercentFormatter(1))

    plt.show()
    plt.boxplot(dist)
    plt.show()
    count += 1

