

import csv
import os

def save(rev_type, file, dist, change_x, change_y):
        ''' saves row into new file based on whether there is a reversal or not '''


        with open(os.getcwd() + "\\" + file, 'a', newline="") as nf:    
            
            writer = csv.writer(nf)                                                         
            row = [dist, change_x, change_y]                               
            writer.writerow(row)

def main():


    files = ['rev_new_n2_3_d1_schafer.csv', 'rev_new_daf2_3_d17_schafer.csv']

    for file in files:

        with open(os.getcwd() +"\\" + file, 'r') as cf:

            read = csv.reader(cf, delimiter=',')

            for row in read:

                if row[1] == 'NR':

                    save('NR', 'NR' + file, row[3], row[4], row[5])

                elif row[1] == 'R':

                    save('R', 'R' + file, row[3], row[4], row[5])


main()
                
