#create a file that contain 1000 lines of random strings
import random as r
import string as s
s=s.ascii_letters

fp=open('result.txt','w')
for i in range(0,1000):
    fp.write("".join(r.sample(s,4))+"-"+"".join(r.sample(s,4))+"-"+"".join(r.sample(s,4))+"-"+"".join(r.sample(s,4))+"\n")
fp.close()