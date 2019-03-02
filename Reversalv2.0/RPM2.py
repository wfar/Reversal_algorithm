# python 3
# RPM class used to calculate number of reversals per minute
# made by C. elegans based on the data created from total reversals
# in a sequence of time


import csv
import math
import os

class RPM:
    ''' RPM class takes the data set created from the reversal count and tallies up
        the number of reversal per minute and saves them into a new data file
        '''
    
    def __init__(self):
        ''' constructor used to create map to hold number of reversals in each minute'''
        self.holder = {}    


    def write_to_file(self, name):
        ''' save the count and minute interval into a csv in given file path'''
        
        path = os.getcwd() + '\\reversals_per_minute\\'                                 # path to new data set folder
        with open(path + 'revpm_' + name, 'a', newline="") as nf:                       # open a csv file for corresponding new data set
            
            writer = csv.writer(nf)                                                     # creates csv writer object
            for key in self.holder.keys():
                row = [key, self.holder.get(key)]
                writer.writerow(row)                                                    # write row to the csv

    def run(self):
        ''' run() method executes the entire rpm conversion
            process for each file
            '''

        print("Started rpm conversion")

        files = os.listdir(os.getcwd() + '\\full_data_2fps')                            # get all files in the directory

        for file in files:                                                              # iterate through each file                                                

            name = file[4:]                                                             # save file name
       
            with open(os.getcwd() + '\\full_data_2fps\\' + file, 'r') as cf:            # open current file in loop

                read = csv.reader(cf)                                                   # read file into csv reader
                last = ['NR', '0']                                                      # set intial compare point and store into last which will be updated

                
                for row in read:                                                        # iterate through each row in the file
                    '''
                    if float(row[3]) > 2.5:
                        print(row[3])
                        continue
                    '''
                    
                    if row[2] not in self.holder:                                       # if minute interval not in map, then add it
                        self.holder[row[2]] = 0
                        print(row[2])
                    if last[0] != row[1]:                                               # check if there was a reversal counted 

                        if row[1] == "NR":
                            last[0] = "NR"
                            continue
                        if row[2] in self.holder:                                       # if this minute interval already in map, increment its reversal count by 1
                            self.holder[row[2]] += 1
                        else:
                            self.holder[row[2]] = 1                        

                        last[0] = row[1]                                                # change the last value to the current reversal symbol so we dont count the same reversal again

            self.write_to_file(name)                                                    # save map into file                                    
            self.holder.clear()                                                         # clear the objects holder list for next file


        print("Finished rpm conversion")


if __name__ == "__main__":

    test = RPM()
    test.run()
                        
                    
                    

                
