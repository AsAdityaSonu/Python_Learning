#Create 10 files that contains multiple lines of random strings and file size of each file must be 5 MB.
import random as r
import string as s
s=s.ascii_letters+s.digits

file_size=5*1024*1024
for i in range(0,9):
    file_name=input("Enter the name of file ")
    fp=open(file_name,'w')

    current_size=0
    while(current_size<file_size):
        random_string=''.join(r.choice(s))
        fp.write(random_string)
        current_size+=len(random_string)
    fp.close()
    
