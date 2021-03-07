import datetime
from zipfile import ZipFile 
import os
import redis
current_date1 = datetime.datetime.now().strftime("%d%m%y")
redis_instance = redis.StrictRedis(host='localhost',
                                  port=6379, db=0)


current_date = "020321"
print("Current date",current_date1)


bhav_url = 'https://www.bseindia.com/download/BhavCopy/Equity/EQ%s_CSV.ZIP'%current_date1

if os.system("wget %s"%bhav_url) == 0:


  
    # specifying the zip file name 
    file_name = "EQ%s_CSV.ZIP"%current_date1
    
    # opening the zip file in READ mode 
    with ZipFile(file_name, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 
    
        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall() 
        print('Done!') 


    import csv

    with open('EQ020321.CSV') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        
        line_count = 0
        for row in csv_reader:
        
            redis_instance.hmset(row[1].strip(),{'code':row[0],'open':row[4],'high':row[5],'low':row[6],'close':row[7]})
            line_count +=1
        print(line_count)    
        