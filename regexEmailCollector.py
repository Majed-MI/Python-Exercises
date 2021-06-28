# collecting all emails from a huge string and storing it in a file.txt
# importing regular expression
import re
# the string huge
str = """
        Hello Bro my name is Majed. my official email id is: majedifti@gmail.com, And i am learning Programming
        on CodeWithHarry Youtube channel. i am so much interested in Python and javascript. You can 
        contact me on another email: majedmahmud1998@gmail.com. Also there is a student edumail in
        which you can contact through:majed1803052@stud.kuet.ac.bd you can also contact in these email
        too: majjodi_mj_ 98@gmail.com. And you can alse contact my fathers gmail: mahmud964@gmail.com
        and the channel email is: harrybhai@codewithharry.com
       """
# email finding regex
list = re.findall(r"\w+@\S+\w",str)
# opening the txt file
op = open("email_store.txt","a")
# initializing the j to show the email in a serial numeric way
j=1
for i in list:
    # writing the email's one by one in the file.txt
    op.write(f"Email {j} : {i}\n")
    # j++ to maintain serial
    j=j+1

# closing the file
op.close()

# printing the emails
print(f"Emails are: {list}")
# total email number
print(f"Total Emails are: {j-1}")