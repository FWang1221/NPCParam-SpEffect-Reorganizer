import csv
import time
#requires python 3.1
mainCSV = []

yourCSVFile = input("Please enter the name of the NPCparam CSV you wish to reorder the spEffectIDs of (don't need to say .csv). Preferably, put the file in the same directory as me (or the other way around) for ease of access. \n")

with open(yourCSVFile + ".csv", newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        mainCSV.append(row)
headers = mainCSV[0]
spEffectIndex = []
numedits = 0

print("Please wait while I reorder your spEffectIDs.")

for x in range(0, 32): #0-31
    spEffectIndex.append(headers.index("spEffectID" + str(x)))

for x in range(0, 32):
    for x in range(0, len(spEffectIndex) - 1):
        currentInd = spEffectIndex[x]
        nextInd = spEffectIndex[x + 1]
        for row in range(1, len(mainCSV)):
            currentRow = mainCSV[row]
            if currentRow[currentInd] == "0" or currentRow[currentInd] == "-1" or currentRow[currentInd] == "change":
                if currentRow[nextInd] != "0" or currentRow[nextInd] != "-1":
                    mainCSV[row][spEffectIndex[x]] = mainCSV[row][spEffectIndex[x+1]]
                    mainCSV[row][spEffectIndex[x+1]] = "-1"
                    numedits += 1

with open(yourCSVFile + "Corrected.csv", "w", newline="") as csvfile:
    npcwriter = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_NONE)
    for row in range(0, len(mainCSV)):
        npcwriter.writerow(mainCSV[row])
print("Done. " + str(numedits) + " were made to reorganize your NPCparam's spEffectIDs. These edits were written to a file called " + yourCSVFile + "Corrected.csv")

time.sleep(5)

quit()

