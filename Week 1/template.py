import sys
import os
filein = open("template.in", "r")
fileout = open("template.out", "w")
inputs = filein.readline().split()
width = int(inputs[0])
height = int(inputs[1])
mapa = {}
languageResult = ""
auxChar = ""
minResult = sys.maxsize
auxCounter = 1
#print("min", min(minResult, 100))
for i in range(height):
    row = filein.readline().strip('\n')
    #print("row len", len(row))
    for j in range(width):
        mapa[row[j]] = {"x": i + 1, "y": j + 1}
filein.readline()
for i in range(3):
    auxLang = filein.readline()
    #print("aux lang", auxLang)
    sum = 0
    row = filein.readline().strip('\n')
    #print("row == begin", row == "begin")
    lineCounter = 0
    while len(row) > 0:
        if lineCounter > 0:
            #print("last char adding: ", row[0], "and", auxChar, "result", max((abs(mapa[row[0]]["x"] - mapa[auxChar]["x"])), (abs(mapa[row[0]]["y"] - mapa[auxChar]["y"]))))
            sum += max((abs(mapa[row[0]]["x"] - mapa[auxChar]["x"])), (abs(mapa[row[0]]["y"] - mapa[auxChar]["y"])))
        auxChar = row[len(row) - 1]
        #print("aux char", auxChar)

        auxCounter += 1
        for x in range (len(row) - 1):
            #print("adding: ", row[x], "and", row[x + 1], "result:", max((abs(mapa[row[x + 1]]["x"] - mapa[row[x]]["x"])), (abs(mapa[row[x + 1]]["y"] - mapa[row[x]]["y"]))))
            sum += max((abs(mapa[row[x + 1]]["x"] - mapa[row[x]]["x"])), (abs(mapa[row[x + 1]]["y"] - mapa[row[x]]["y"])))

        row = filein.readline().strip('\n')
        lineCounter += 1
    #


    # print("sum", sum)
    if sum < minResult:
        minResult = sum
        languageResult = auxLang
fileout.write(languageResult)
fileout.write(str(minResult))
filein.close()
fileout.close()