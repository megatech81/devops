#!/usr/bin/env python
import random
length_otp =6
x=length_otp
min =0
max =9
i=0
list_otp=[i for i in range(20)]
while length_otp > 0 :
    list_otp[i]=random.randint(min, max)
    i+=1
    length_otp=length_otp-1
otp =list_otp[:x]
otp_format="your otp:{0}{1}{2}{3}{4}{5}".format(otp[0],otp[1],otp[2],otp[3],otp[4],otp[5])
print(otp_format)
user_responce =input("enter your otp with spaces:")
if user_responce == str(otp_format) :
    print("WELCOME TO HELLO WORLD")
    import matplotlib.pyplot as plt
    x= [1,2,3,4,5,6]
    y =[100,101,102,103,104,105]
    plt.plot(x,y)
    plt.show()
else:
    print("PLEASE ENTER CORRECT OTP")


