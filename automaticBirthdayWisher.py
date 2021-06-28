# Automatic Birthday wisher From Email
# importing modules
import pandas as pd
import datetime
import smtplib
import os
# change directory
os.chdir("C:\\Users\\iftekhar\\Desktop\\Programing\\Python PROGRAM\\PROGRAM")

# Enter your authentication details
Gmail_Id = ''
Gmai_Password = ''

# sendEmail function with to subject and msg value
def sendEmail(to,sub,msg):
    print(f"Email to {to} sent with subject : {sub} and message {msg}")
    # email syntax
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.starttls()
    s.login(Gmail_Id,Gmai_Password)
    s.sendmail(Gmail_Id,to,f"Subject:{sub}\n\n{msg}")
    s.quit()

# only applicable under this function
if __name__ == '__main__':
    # this is the function when it is called it will send email
    # sendEmail(Gmail_Id,"subject","text message")
    # exit()
    # but for sending email u have to make email less secured

    # taking the datas from the excel file
    df = pd.read_excel("Mybirthdaylist.xlsx")
    # print(df)
    # getting the date in date month format and year format
    today  = datetime.datetime.now().strftime("%d-%m")
    yearNow  = datetime.datetime.now().strftime("%Y")
    # print(today)
    # declaring an empty list to entry data from here to update
    writeInd = []
    # for all the birthday dates find the matched date of today
    for index,item in df.iterrows():
        # print(index,item['Birthday'])
        bday = item['Birthday'].strftime("%d-%m")
        # print(bday)
        # if birthday date and today date is same and not wished yet in the year then sendemail and also
        # append the year in the list of writeInd
        if (today == bday) and yearNow not in str(item['Year']):
            sendEmail(item['Email'],"Happy Birthday",item['Dialogue'])
            writeInd.append(index)
    # now print the list of the years when wished
    print(writeInd)

    # for the list of writeInd append the year in the excel file
    for i in writeInd:
        # lock the year in the excel file
        yr = df.loc[i,'Year']
        # print(yr)
        # append the year in one by one ',' format
        df.loc[i,'Year'] = str(yr) + "," + str(yearNow)
        # print(df.loc[i,'Year'])

    # print(df)
    # to prevent unnamed list order
    df.to_excel('Mybirthdaylist.xlsx',index=False)

