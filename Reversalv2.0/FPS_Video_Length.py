# python 3.7
# Script to read and determine the range in fps
# as well to find out the range in video length

import os
import csv



class FPS_Video_Length:

    def __init__(self):
        pass



    def save(self, file, length, fps):

        with open(os.getcwd() + "\\full_data_2fps\\range_fps_length.csv", 'a', newline="") as nf:    
            
            writer = csv.writer(nf)                                                         
            row = [file, length, fps]                               
            writer.writerow(row)
        


    def run(self):
        
        files = os.listdir(os.getcwd() + '\\2_down_sampling')

        for file in files:
            print(file)
            with open(os.getcwd() + '\\2_down_sampling\\' + file, 'r') as cf:

                read = csv.reader(cf, delimiter=',')

                row_count = sum(1 for row in read)
                row_count += 1

            with open(os.getcwd() + '\\2_down_sampling\\' + file, 'r') as cf2:

                read = csv.reader(cf2, delimiter=',')
                count = 1
                
                for row in read:
                    
                    count += 1
                    
                    if count == row_count:
                        fps = row[3]
                        self.save(file[4:], float(row[0]) / float(fps) , fps)
                        print("Saved")
                        
if __name__ == "__main__":

    test = FPS_Video_Length()
    test.run()
