from time import *
import random as r


def mistake(paratest,usertest):
    error = 0
    for i in range(len(paratest)):
        try:
            if paratest[i] != usertest[i]:
                error = error + 1
        except:
            error = error + 1
    return error

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_R = round(time_delay,2)
    speed = len(userinput)/time_R
    return round(speed)


test = ["Select and recommend suitable candidates through professionalism and competence in the Punjab Public Service",
        "My name is faizan and am the fastest man alive","Welcome back to my channel"]

test1 = r.choice(test)

print("*** THIS IS A TYPING SPEED TEST ***")
print(test1)
print()
print()
time_1 = time()
testinput = input("Enter: ")
time_2 = time()

print("Speed: ", speed_time(time_1,time_2,testinput), "w/sec")
print("Error: ", mistake(test1,testinput))