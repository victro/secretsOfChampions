import sys
import os
import math
filein = open("prepare.in", "r")
fileout = open("prepare.out", "w")
N = int(filein.readline())
practice = [int(n) for n in filein.readline().split()]
theory = [int(n) for n in filein.readline().split()]
maxpractice = -1
maxtheory = -1
minpractice = 1001
mintheory = 1001
mindiff = 1002
mindiffindex = -1
minpracticeindex = -1
mintheoryindex = -1
sum = 0
practiceflag = False
theoryflag = False
greaterindex = -1
for i in range(N):
    if maxpractice < practice[i]:
        maxpractice = practice[i]
    if maxtheory < theory[i]:
        maxtheory = theory[i]
    if mintheory > theory[i]:
        mintheory = theory[i]
        mintheoryindex = i
    if minpractice > practice[i]:
        minpractice = practice[i]
        minpracticeindex = i
for i in range(N):
    if practice[i] > theory[i]:
        sum+= practice[i]
        practiceflag = True
        if practice[i] - theory[i] < mindiff and greaterindex < theory[i]:
            mindiff = practice[i] - theory[i]
            mindiffindex = i
            greaterindex = theory[i]
    elif theory[i] > practice[i]:
        sum += theory[i]
        theoryflag = True
        if theory[i] - practice[i] < mindiff and greaterindex < practice[i]:
            mindiff = theory[i] - practice[i]
            mindiffindex = i
            greaterindex = practice[i]
    else:
        sum += theory[i]
        theoryflag = True
        practiceflag = True
if practiceflag == True and theoryflag == True:
    fileout.write(str(sum))
else:
    if practiceflag == False:
        sum -= theory[mindiffindex]
        sum += practice[mindiffindex]
    else:
        sum -= practice[mindiffindex]
        sum += theory[mindiffindex]
    fileout.write(str(sum))

filein.close()
fileout.close()