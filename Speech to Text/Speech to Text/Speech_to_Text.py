from os import listdir
directory = ""
fileNames = listdir(directory)

import speech_recognition as sr

f = open(directory + "\\Voiceline Text.csv", 'w')

for fileName in fileNames:
    r = sr.Recognizer()

    audio = sr.AudioFile(directory + "\\" + fileName)

    with audio as source:
        audio = r.record(source)                  
        result = r.recognize_google(audio, None, "en-US", 0, True, True)
    
    #print(result["alternative"][0]["transcript"] + "," + str(result["alternative"][0]["confidence"]))

    values = ""
    try:
        values = result["alternative"][0]["transcript"] + "," + str(result["alternative"][0]["confidence"])
    except:
        values = "error"

    f.write(fileName + "," + values + "\n")

f.close()