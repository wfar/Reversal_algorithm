# python 3
# RPM class used to calculate number of reversals per minute
# made by C. elegans based on the data created from total reversals
# in a sequence of time


import csv
import math
import os
import datetime

class Rev_TF:
    ''' RPM class takes the data set created from the reversal count and tallies up
        the number of reversal per minute and saves them into a new data file
        '''
    
    def __init__(self):
        ''' constructor used to create map to hold number of reversals in each minute'''
        self.holder = {}    


    def write_to_file(self, name, frame, time, group):
        ''' save the count and minute interval into a csv in given file path'''
        
        path = os.getcwd() + '\\reversals_time_frame\\'                                 # path to new data set folder
        with open(path + 'revtf_' + name, 'a', newline="") as nf:                       # open a csv file for corresponding new data set
            
            writer = csv.writer(nf)                                                     # creates csv writer object
            row = [frame, time, group]
            writer.writerow(row)                                                    # write row to the csv

    def run(self):
        ''' run() method executes the entire rpm conversion
            process for each file
            '''

        print("Started time frame conversion")

        files = os.listdir(os.getcwd() + '\\full_data_2fps')                            # get all files in the directory

        for file in files:                                                              # iterate through each file                                                
            print("running file: " + str(file))
            name = file[4:]                                                             # save file name
       
            with open(os.getcwd() + '\\full_data_2fps\\' + file, 'r') as cf:            # open current file in loop

                read = csv.reader(cf)                                                   # read file into csv reader
                last = ['NR', '0']                                                      # set intial compare point and store into last which will be updated
                group = 0
                
                for row in read:                                                        # iterate through each row in the file
                  
                    if last[0] != row[1]:

                        if row[1] == "NR":
                            last[0] = "NR"
                            group += 1
                        else:                        
                            seconds = float(row[0]) / 23
                            time = str(datetime.timedelta(seconds = seconds))
                            frame = row[0]
                            self.write_to_file(name, frame, time, group)
                            last[0] = row[1]
                            
                    if row[1] == "R":
                        self.write_to_file(name, frame, time, group)



        print("Finished time frame conversion")


if __name__ == "__main__":

    test = Rev_TF()
    test.run()
                        
                    
                    

                
