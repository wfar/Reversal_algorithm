#python 3
#Table counter class (RevFull) used to calculate number of reversals
# made by C. elegans as well as most recent distance between pts,
#change in x, and change in y. Uses original fps.


import csv
import math
import os



class FrameFiler:

    def __init__(self):
        pass

    def dist(self, lis, x, y):
        ''' dist fx calculates the distance between 2 points and returns
            the distance'''
        
        x1, y1, x2, y2 = float(lis[0][0]), float(lis[0][1]), float(x), float(y)     # convert string values into correct point values
        distance = ( ((x2-x1)**2) + ((y2-y1)**2) ) ** (1/2)                         # calculate distance between two points


        return distance     # return distance

    def dist2(self, lis, x, y):
        ''' dist fx calculates the distance between 2 points and returns
            the distance'''

        x1, y1, x2, y2 = float(lis[0]), float(lis[1]), float(x), float(y)   # convert string values into correct point values
        distance = ( ((x2-x1)**2) + ((y2-y1)**2) ) ** (1/2)                 # calculate distance between two points


        return distance     # return distance




    def check(self, x, y, last, fn, file):
        
        cur_d = self.dist(last, x, y)

        frame_t = ""
        if cur_d > 10:
            frame_t = "B"
        else:
            frame_t = "G"

        self.write_to_file(fn, cur_d, x, y, frame_t, file)


    def write_to_file(self, fn, cur_d, x, y, frame_t, file):

        path = os.getcwd() + '\\full_data_2fps\\'                          
        with open(path + 'full_2DS' + file, 'a', newline="") as nf:   


            writer = csv.writer(nf)                                          
            row = [fn, cur_d, x, y, frame_t]           
            writer.writerow(row)

    def write_to_file_2(self, fn, file, rev, mint):

        path = os.getcwd() + '\\full_data_2fps_end\\'                          
        with open(path + 'count_' + file, 'a', newline="") as nf:   


            writer = csv.writer(nf)                                          
            row = [fn, rev, mint]           
            writer.writerow(row)
        
        
    def exe_SA(self):

        print("Running schafer's Algo")
        files = os.listdir(os.getcwd() + '\\full_data_2fps')
        print(len(files))
        lis = []

        
        for file in files:
        
            with open(os.getcwd() + '\\full_data_2fps\\' + file, 'r') as nf:   


                read = csv.reader(nf, delimiter=',')                                          

                count = 0
                for row in read:
                   
                    if row[0] == 'frame_no' or row[0] == '0':
                        count += 1
                        continue

                    if row[4] == 'B':
                        lis.clear()
                        count += 1
                        continue

                    if len(lis) < 20:
                        lis.append([row[2],row[3]])
                        count += 1
                        continue

                    rev = ''
                    
                    cur_d = self.dist2(lis[-1], row[2], row[3])
                   
                    for i in lis[-2::-1]:

                        prev_d = self.dist2(i, row[2], row[3])
                        if cur_d > prev_d:
                            rev = 'R'
                            break

                        rev = 'NR'

                    self.write_to_file_2(row[0], file, rev, count // 120)

                    
                    del lis[0]
                    lis.append([row[2],row[3]])

                    count += 1

        print("Finished")

    def run(self):

        print("Start")
        
        files = os.listdir(os.getcwd() + '\\2_down_sampling')           # get dir name with all sample files

        for file in files:                                             # loop through all list fo files
            
            name = file[4:]                                                # get the name of individual files and clean of the start of it

        #test sample -- 2 FPS down sample!!  ---- os.getcwd() + '\\2_down_sampling\\'+ 'new_n2_9_d10.csv'           actual files --- os.getcwd() + '\\2_down_sampling\\' + file
        
            with open(os.getcwd() + '\\2_down_sampling\\' + file , 'r') as cf:        # open the current file name and read in 

                read = csv.reader(cf, delimiter=',')                        # use csv reader to read file into read comma delimited

                mint = 0            # set mint to count the number of minutes passed- once it is 120, it means one minute passed
                count = 0           # use count to count the number of centroids ( to determine last 20 centroids )


                with open(os.getcwd() + '\\full_data_2fps\\' + 'full_2DS' + file, 'w', newline="") as nf:   # open a csv file for corresponding new data set
        
                    
                    writer = csv.writer(nf)                                         
                    header = ["frame_no", "distance", "centroid_x", "centroid_y", "Frame_type"]
                    writer.writerow(header)



                last = [[0,0]]
                
                for row in read:    # for each row in the file, iterate through

                    

                    if count == 0:  # if it is the first row, increment count and continue since it is the headers
                        count += 1
                        mint += 1
                        continue


                    fn = row[0]                                                 
                    self.check(row[1], row[2], last, fn, file)
                    last = [ [row[1],row[2]] ]
                            
                        
                    count += 1             
                    mint += 1               
     
            
        
        print("Finished")
        


if __name__ == "__main__":

    test = FrameFiler()
    test.run()
    test.exe_SA()
    

        
