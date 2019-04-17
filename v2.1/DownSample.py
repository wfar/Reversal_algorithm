

import pandas
import os
import csv





def get_fps():

    log = pandas.read_csv('log.txt', sep = " ", header = None)

    log.columns = ["Frame", "Time", "x", "y", "z"]
    

    total_frames = len(log["Frame"])
    
    min_time = log["Time"][0]
    max_time = log["Time"][total_frames-1]
    
    fps = total_frames // ((max_time - min_time) / 1000)
    
    
    return fps
    
    





def down_size(fps, y):
    
    ds = fps # //2
    
    feat = pandas.read_csv('feature.log', sep=",", header = None)
    feat.columns = ["FN", "x", "y", "area"]
    
    index_arr = []
    
    cur = ds
    count = 0
    index = 0
    run_avg = [0,0,0,0]
    
    while (True):
        
    
        while count < cur:
            
            #print("this is count: " + str(count))
            
            try:
                run_avg[0] += feat["x"][index]
                run_avg[1] += feat["y"][index]
                
                #print(index)
                
                count += 1
                index += 1
                
                
            except:
                print("This is the end: " + str(index))
                break

            
    
        final_avg = [index,(run_avg[0] / ds), (run_avg[1] / ds), fps ]
        
        
        index_arr.append(final_avg)
        
        
        count = 0
        run_avg = [0,0,0,0]
        
   
        if index == len(feat["FN"]):
            break
    
    
    
    with open('E:\\2_down_sampling\\new_' + y +'.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=',')
        
        headers = ['Frame_number', 'X', 'Y', 'old_fps']
        writer.writerow(headers)
        
        for s in index_arr:
        
            writer.writerow(s)
            
            
    
            



def run(y):
    
    fps = get_fps()
    down_size(fps, y)
    
    
    





def main():
    
    path_to = '//CDM-MEDIXSRV/Nematodes/data'
    os.chdir(path_to)
    
    my_files = ['daf2_1','daf2_2','daf2_3','daf2_4','daf2_5', 'daf2_6','daf2_7','daf2_9','daf2_10','n2_1','n2_2','n2_3',
               'n2_4','n2_5','n2_6','n2_8','n2_9','n2_10']
    
    
    file_list = os.listdir()
    
    #print(file_list)
    
    
    print("hello")
    for x in my_files:
        
        for y in file_list:
            
            if x in y:
                
                new_path = path_to + '/' + y + '/log'
                os.chdir(new_path)
                run(y)
                
    print("New files created")
        



main()







