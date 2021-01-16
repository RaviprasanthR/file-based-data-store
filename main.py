import json
import sys
import os
import time

data={} #dictionary to store the data

user_choice=input("Do you want to save the file in the default location(Y/N)?")
if(user_choice=="Y" or user_choice=="y"):
    file_path="D:\\file based data store\\data.json" 
elif(user_choice=="N" or user_choice=="n"):
    file_path=input("Enter the new location (Eg: D:\\freshworks-assignment\\newone.json)")

def file_size_check(file_path): #this function checks if the file size is less than 1GB
    path=os.stat(file_path)     #file_path denotes the location of the file
    size=path.st_size           #size of the file is stored in the variable size
    if(size<(1024*1024*1024)):  #checking if the file size is less than 1GB
        return True             #returns True if the file size is less than 1GB
    else:
        return False            #returns False if the file size is greater than 1GB

def value_size_check(value):        #function to check if the value given is less than 16KB
    json_string=json.dumps(value)   #converts dictionary into string
    size=sys.getsizeof(json_string) #size of the value is stored in the variable size
    if(size/1024<16):               #checks if the size of the value is less than 16KB
        return True                 #returns True if the size is less than 16KB
    else:
        return False  

def write_json(data,filepath):
    with open(filepath,'w')as f:
        json.dump(data,f,indent=4)


def create(key,value,timetolive):
    if(key in data):
        print("ERROR : The given key already exists")
    else:
        if(key.isalpha()):
            if(file_size_check(file_path) and value_size_check(value)):
                if(timetolive==0):
                    temp=[value,timetolive]
                else:
                    temp=[value,time.time()+timetolive]
                if len(key)<=32:
                    data[key]=temp 
                    
                #with open(file_path) as json_file:
                    #json_data=json.load(json_file)
                    #temp_data=json_data['data_store']
                    #temp_data.append(data)

                #write_json(data,file_path)
                              
            else:
                print("ERROR : Memory limit exceeded 1GB")
        else:
            print("ERROR : Invalid Key ! Key must be a string")
        
                

def read(key):
    if key not in data:
        print("ERROR : The given Data does not exist. Please enter a valid Key") #error message4
    else:
        read=data[key]
        if read[1]!=0:
            if time.time()<read[1]: #comparing the present time with expiry time
                with open(file_path,'r') as rf:
                    json_read=json.load(read,rf)
                    return json_read
                    
            else:
                print("ERROR: time-to-live of",key,"has expired") #error message5
        else:
            with open(file_path,'r') as rf:
                json_read=json.load(read,rf)
                return json_read


create('ravi',23,4)
print(data)