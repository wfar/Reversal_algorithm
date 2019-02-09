#python 3
#Reversal class used to calculate number of reversals
# made by C. elegans

import csv
import math
import os



class Rev:
    ''' Rev class creates an object to encapulate the total reversals
        made within a given data set. It is set up so as to read in all
        the data files from our set'''
    
    def __init__(self):
        ''' initilize reversal value to 0 and create a centroid list
            to hold the last 19 centroids'''
        
        self.rev = 0
        self.clist = []

    def dist(self, lis, x, y, fn):
        ''' dist fx calculates the distance between 2 points and returns
            the distance'''
        #print(fn, lis, x, y)
        x1, y1, x2, y2 = float(lis[0]), float(lis[1]), float(x), float(y)
        distance = ( ((x2-x1)**2) + ((y2-y1)**2) ) ** (1/2)


        return distance

            

    def check(self, x, y, fn):
        ''' check fx is used to compare the current centroids distance to
            the last centroid and test it agaisnt the distance of all the
            last 19 centroids to see if there is a reversal (Scheifer algorithm)
        '''
        
        cur_d = self.dist(self.clist[-1], x, y, fn )

        for i in self.clist[:-2]:

            prev_d = self.dist(i, x, y, fn)

            if cur_d > prev_d:
                    self.rev += 1
                    break

    def save_to_file(self, f_name, minute):
        ''' saves reversal count to the current minute in the new csv '''
        
        path = os.getcwd() + '\\reversals_minute\\'
        with open(path + 'rev_' + f_name, 'a', newline="") as nf:
            
            writer = csv.writer(nf)

            print(self.rev)
            row = [minute // 300, self.rev]
            writer.writerow(row)         


        

    def run(self):
        ''' runs the entire reversal counting process for the object
        '''
        print("Counting started")
        files = os.listdir(os.getcwd() + '\\down_sampling')


        for file in files:
            print(file)
            head = file.split("_")
            name = file[4:]
            
            # not used just yet
            headers = [head[1], head[2], head[3], 0, 0, 0]


            #hello = os.getcwd() + '\\down_sampling\\'+ 'new_daf2_10_d8.csv'           os.getcwd() + '\\down_sampling\\' + file
            with open(os.getcwd() + '\\down_sampling\\' + file, 'r') as cf:

                read = csv.reader(cf, delimiter=',')

                mint = 0
                count = 0
                
                for row in read:

                    if count == 0:
                        count += 1
                        continue
                        
                    if count < 20:
                        self.clist.append( [row[1], row[2]] )
                        count += 1
                        mint += 1
                        continue

                    fn = row[0]
                    self.check(row[1], row[2], fn)

                    del self.clist[0]
                    self.clist.append( [row[1], row[2]] )
                    count += 1
                    mint += 1

                    if mint % 300 == 0:
                        self.save_to_file(name, mint)
                        self.rev = 0

            self.clist.clear()
        
            print(self.clist)
            print("Reversal counting for COMPLETE: " + str(self.rev) + file)
            print(count)

            
      

if __name__ == "__main__":

    test = Rev()
    test.run()
    
    
    

                

                    
