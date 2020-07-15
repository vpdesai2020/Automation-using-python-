#Author : Vasanth Kumar Desai

#Requirements: math, random


#---------------------------------------------------------------------#

import math,random
def otp_generator():
    num="0123456789"
    OTP=""

    for i in range(4): #lenght of OTP want to generate
        OTP+=num[math.floor(random.random()*10)]
    print(OTP)

otp_generator()
