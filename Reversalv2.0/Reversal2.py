# python 3
# schafer's algorithm modified to use a threshold 
# v1.0


import os
import csv
import RPM



class Reversal2:

    def __init__(self):
        ''' constructor for reversal object '''
        
        self.prev_centroid = []                                                             # stores the curret number of centroids per file

    def dist(self, lis, x, y ):
        ''' dist fx calculates the distance between 2 points and returns
            the distance'''
        
        x1, y1, x2, y2 = float(lis[0]), float(lis[1]), float(x), float(y)                   # convert string values into correct point values
        distance = ( ((x2-x1)**2) + ((y2-y1)**2) ) ** (1/2)                                 # calculate distance between two points


        return distance                                                                     # return distance


    def check_rev(self, x, y):
        ''' runs modified shafers algorithm on centroids using a given threshold '''
        
        dist_from_cur_to_prev = self.dist(self.prev_centroid[-1], x, y)                     # mesuare distane from current centroid to most recent past centroid

        for i in self.prev_centroid[-2::-1]:                                                # iterate through all ther previous centroids

            dist_from_cur_to_others = self.dist(i, x, y)                                    # calclulate the distacnce frm thee previous centroids with current centroid

            if 10 > dist_from_cur_to_prev - dist_from_cur_to_others > 3.0:                       # this is the current threshold value

                return True                                                                 # returns true if reversal occurred
            
        return False                                                                        # returns false if no reversal occurred


    def save(self, file, frame_num, rev, minute_interval):
        ''' saves row into new file based on whether there is a reversal or not '''
        
        with open(os.getcwd() + "\\full_data_2fps\\rev_" + file, 'a', newline="") as nf:  # open file in new folder to store reversal count in a given frame per minute interval
            
            writer = csv.writer(nf)                                                         # creates csv writer object
            row = [frame_num, rev, minute_interval]                                         # create row for csv including minute number and the current count for reversals
            writer.writerow(row)                                                            # write row 
                


    def run(self):
        ''' run() reads all log files in given folder, calculates reversals
            and saves the count into new files to be used with RPM.py'''
            
        print("Started reversal count")
        files = os.listdir(os.getcwd() + '\\2_down_sampling')                                  # get dir name with all sample files

        test1 = 25

        for file in files:                                                                  # loop through all list fo files
            
            with open(os.getcwd() + '\\2_down_sampling\\' + file, 'r') as cf:                  # open the current file name and read in 

                read = csv.reader(cf, delimiter=',')                                        # use csv reader to read file into read comma delimited

                count = 0                                                                   # use count to count the number of centroids ( to determine last 20 centroids )
                
                for row in read:                                                            # for each row in the file, iterate through

                    if count == 0:                                                          # if it is the first row, increment count and continue since it is the headers
                        count += 1
                        continue
                        
                    if count <= 20:                                                         # if count is less than 20, we increment count and add the centroid to our passing window
                        self.prev_centroid.append( [row[1], row[2]] )
                        count += 1
                        continue
                    
                    frame_num = row[0]                                                 
                    rev = self.check_rev(row[1], row[2])   

                    minute_interval = (count // 120)
                    if rev:
                        self.save(file, frame_num, 'R', minute_interval )
                    else:
                        self.save(file, frame_num, 'NR', minute_interval )

                    
                    if count >= 20:                                                         # checks to see if we just calclulated a reversal, if not then delete the 20th centroid from list, and add the newest centroid to list
                        del self.prev_centroid[0]
                        self.prev_centroid.append( [row[1], row[2]] )
                        
                    count += 1                                                              # increment count so we can continue counting the next centroid


            self.prev_centroid.clear()                                                      # current file complete, clear objects list to prepare for next files
##            test1 -= 1
##            if test1 == 0:
##                break
            
        print("Finished reversal count")



if __name__ == "__main__":

    test = Reversal2()
    test.run()
    rpm = RPM.RPM()
    rpm.run()
    
    

    
