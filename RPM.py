#python 3
#RPM class used to calculate number of reversals oer minute
# made by C. elegans based on the data created from total reversals
# in a sequence of time


import csv
import math
import os

class RPM:

    def __init__(self):
        
        self.holder = {}


    def write_to_file(self, name):

        path = os.getcwd() + '\\reversals_per_minute\\'     # path to new data set folder
        with open(path + 'revpm_' + name, 'a', newline="") as nf:   # open a csv file for corresponding new data set
            
            writer = csv.writer(nf)                 # creates csv writer object
            for key in self.holder.keys():
                row = [key, self.holder.get(key)]
                writer.writerow(row)                # write row to the csv

    def run(self):

        files = os.listdir(os.getcwd() + '\\reversals_minute')

        for file in files:

            name = file[4:]
            
            with open(os.getcwd() + '\\reversals_minute\\' + file, 'r') as cf:

                read = csv.reader(cf)
                last = ['NR', '0']
                rev_count = 0
                
                for row in read:

                    if last[0] != row[0]:

                        if row[1] in self.holder:
                            self.holder[row[1]] += 1
                        else:
                            self.holder[row[1]] = 1                        

                        last[0] = row[0]

            self.write_to_file(name)
            self.holder.clear()


if __name__ == "__main__":

    test = RPM()
    test.run()
                        
                    
                    

                
