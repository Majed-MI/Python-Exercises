# Health management software and taking the data and entering the data to .txt file and directing nicely
client_list = {1:"Rashed",2:"Majed",3:"Rayed"}
log_list = {1:"Exercise", 2:"Diet"}

# getdate function
def getdate():
    # datetime module
    import datetime
    # returning so when needed using function will be printed the return value
    return datetime.datetime.now()

# try to do these if error occurs then alse it will run
try:
    print("Select Client Name: ")
    # for key and values in dictionary print press the number for the client names as serial
    for key,value in client_list.items():
        print("Press",key,"For",value,"\n",end="")
    # taking input as integer for the clients
    client_name = int (input())
    # printing selected client name
    print("Selected Client: ",client_list[client_name],"\n",end="")
    
    print("Press 1 for log")
    print("Press 2 for retrieve")
    # choice 1 for log and 2 for retrieve
    op = int (input())
    
    if op == 1:
        # choosing the activitiy for the log 
        for key,value in log_list.items():
            print("Press",key,"to log",value,"\n",end="")
        # choice for exercise or diet
        log_name = int (input())
        print("Selected Activity: ",log_list[log_name])
        
        # opening file in the name of client and log name and creating .txt file and appending
        f = open(client_list[client_name]+"_"+log_list[log_name]+".txt","a")
        # declaring k var as y to continue the loop if it is not n
        k='y'
        # continuing the loop if not n is given as input for k
        while(k != "n"):
            # taking input for the loggging in .txt file and storing data
            print("Enter",log_list[log_name],"\n",end="")
            mytext = input()
            # storing the data in date format with the text of logging
            f.write("["+str(getdate())+"]:" + mytext + "\n")
            # input taking if the user want to add more or not
            k = input("Add more? y/n:")
            # continue if not n
            continue
        # closing the file
        f.close()

    elif op == 2:
        # option 2 for retrieving which means getting the stored data from the file
        for key, value in log_list.items():
            print("Press", key, "to retrieve", value, "\n", end="")
        log_name = int(input())
        # printing the stored data for the client and log name given as input
        print(client_list[client_name],"-", log_list[log_name],"Report:","\n",end="")
        # opening the file of the input given and in read format
        f = open(client_list[client_name] + "_" + log_list[log_name] + ".txt", "rt")
        # read the text file one line by one line
        contents = f.readlines()
        # for loop to print more lines from logging
        for line in contents:
            # print the line one by one
            print(line,end = " ")
        # closing the file
        f.close()

    # giving invalid option as input
    else:
        print("Invalid Input")

# error handling if error the print the error format and alse wrong input given to alert the user
except Exception as e:
    print("Wrong Input")
    print(e)


