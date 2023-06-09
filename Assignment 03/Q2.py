#Create a file that contains multiple lines of random strings and file size must be 5MB
import random as r
import string as s

file_size= 5*1024*1024

file_name="Aditya.txt"
#opening file
fp=open(file_name,'w')
current_size=0
while(current_size<file_size):
    random_string=''.join(r.choices(s.ascii_letters))
    fp.write(random_string)
    current_size+=len(random_string)


fp.close()
