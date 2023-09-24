import os

rootPath = "./word_list_raw/"
targetPath = "./word_list/"
for fileIdx in range(1, 48 + 1):
    fileName = "list" + str(fileIdx)
    filePath = rootPath + fileName
    targetFilePath = targetPath + fileName
    fin = open(filePath, 'r')
    fout = open(targetFilePath, 'w')

    # Legalize content format.
    rawLines = fin.readlines()
    for line in rawLines:
        # Remove [inserted]
        insertedIdx = line.index("]") + 2;
        line = line[insertedIdx :]
        # Change the ',' after word as '*'
        line = line.replace(",", "*", 1)
        # Remove [sound:]
        soundIdx = line.find("sound")
        if soundIdx != -1 and line[soundIdx - 1] == '[':
            soundBefore = line[: soundIdx - 1]
            if soundBefore[-1] == " ":
                soundBefore = soundBefore[: -1]
            soundAfter = line[soundIdx :]
            soundEndIdx = soundAfter.index("]") + 1
            soundAfter = soundAfter[soundEndIdx :]
            # Replace the ',' after sound as '*'
            soundAfter = soundAfter.replace(",", "*", 1)
            line = soundBefore + soundAfter
        line = line.replace("<br>", "*")
        line = line.replace("<br />", "*")
        line = line.replace("&nbsp", "")
        fout.write(line)

    # Close files.
    fin.close()
    fout.close()
    print("Legalize list " + str(fileIdx) + " finish!")
