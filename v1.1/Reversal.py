 #python 3
#Reversal class used to calculate number of reversals
# made by C. elegans

import csv
import math
import os




class Rev:
    ''' Rev class creates an object to encapulate the total reversals
        made within a given data set. It is set up so as to read in all
        the data files from our set
    '''
    
    def __init__(self):
        ''' initilize reversal value to 0 and create a centroid list
            to hold the last 19 centroids'''
        
        self.rev = 0        # holds the number of reversals per file
        self.clist = []     # holds the last 20 centroids
        self.rev_list = []

    def dist(self, lis, x, y, fn):
        ''' dist fx calculates the distance between 2 points and returns
            the distance'''
        
        x1, y1, x2, y2 = float(lis[0]), float(lis[1]), float(x), float(y)   # convert string values into correct point values
        distance = ( ((x2-x1)**2) + ((y2-y1)**2) ) ** (1/2)                 # calculate distance between two points


        return distance     # return distance

            

    def check(self, x, y, fn, count, minute, f_name):
        ''' check fx is used to compare the current centroids distance to
            the last centroid and test it agaisnt the distance of all the
            last 19 centroids to see if there is a reversal (Scheifer algorithm)
        '''
        
        cur_d = self.dist(self.clist[-1], x, y, fn )        # calculate the distance from current centroid to its closest previos centroid

        for i in self.clist[-2::-1]:                           # iterate through all other 19 previous centroids (not the closets previous centroid)

            prev_d = self.dist(i, x, y, fn)                 # calculate the distance fro that centroid with current centroid

            if cur_d > prev_d + 1.5:                              # if the distance for last centroid is greater than any other previous centroid, than the new centroid has reversed!
                self.rev += 1                               # increment the reversal count by 1
                self.clist.clear()                          # clear the centroid list so as to not recalculate and reversal again
                count = 0                                   # set count to 0 so we can add the next 20 centroids into our list
                self.rev_list.append(['R',minute // 120])
                self.save_to_file(f_name, minute, fn)
                break
                                           
            else:
                self.rev_list.append(['NR',minute // 120])
                #self.save_to_file(f_name, minute, fn)

        self.save_to_file(f_name, minute, fn)

        return count      # no reversals detected between this set of previous centroids, so we return the original count                  

                    

    def save_to_file(self, f_name, minute, fn):
        ''' saves reversal count to the current minute in the new csv '''
        
        path = os.getcwd() + '\\reversals_minute\\'                          # path to new data set folder
        with open(path + 'rev_' + f_name + ".csv", 'a', newline="") as nf:   # open a csv file for corresponding new data set
            
            writer = csv.writer(nf)                                          # creates csv writer object
            row = [fn, self.rev_list[-1][0], self.rev_list[-1][1]]           #create row for csv including minute number and the current count for reversals
            writer.writerow(row)                                             # write row to the csv



    def run(self):
        ''' runs the entire reversal counting process for the object
        '''
        print("Started")
        files = os.listdir(os.getcwd() + '\\2_down_sampling')           # get dir name with all sample files

        for file in files:                                              # loop through all list fo files
            
            name = file[4:]                                             # get the name of individual files and clean of the start of it

            #test sample -- 2 FPS down sample!!  ---- os.getcwd() + '\\2_down_sampling\\'+ 'new_n2_9_d10.csv'           actual files --- os.getcwd() + '\\2_down_sampling\\' + file
            
            with open(os.getcwd() + '\\2_down_sampling\\' + file, 'r') as cf:     # open the current file name and read in 

                read = csv.reader(cf, delimiter=',')                              # use csv reader to read file into read comma delimited

                mint = 0            # set mint to count the number of minutes passed- once it is 120, it means one minute passed
                count = 0           # use count to count the number of centroids ( to determine last 20 centroids )
                
                for row in read:    # for each row in the file, iterate through

                    

                    if count == 0:  # if it is the first row, increment count and continue since it is the headers
                        count += 1
                        mint += 1
                        continue
                        
                    if count <= 20: # if count is less than 20, we increment count and add the centroid to our passing window
                        self.clist.append( [row[1], row[2]] )
                        count += 1
                        mint += 1
                        continue

                    fn = row[0]                                                 # ignore, pointless
                    count = self.check(row[1], row[2], fn, count, mint, name)   #set counts to either 0 or leaves it the same depending on what check returns
                                                                                # if the new centroid is determined to be a reversal position, count will be 0, and the centroid list will be cleared
                    count = 0
                    if count >= 20:                                             # checks to see if we just calclulated a reversal, if not then delete the 20th centroid from list, and add the newest centroid to list
                        del self.clist[0]
                        self.clist.append( [row[1], row[2]] )
                        
                    count += 1              # increment count so we can continue counting the next centroid
                    mint += 1               # increment to next frame to keep track of minutes
    
                    if mint % 120 == 0:     # checks to see if a minute has passed, if so add the minute number and current reversal count to new csv ( reversal per minuite!!! )
                        #self.save_to_file(name, mint)   
                        self.rev = 0

            self.clist.clear()              # current file complete, clear objects list to prepare for next files

            ### DEBUGGING ###
            #print(self.clist)
            #print("Reversal counting for COMPLETE: " + str(self.rev) + file)
            #print(count)
            
        
        print("Finished")

            
      

if __name__ == "__main__":

    test = Rev()
    test.run()
    
    
    
    

                

                    
