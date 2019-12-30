
import os


fPath = '/Users/mac/Documents/GitHub/PythonDrill/'


def findTxt():
    for file in os.listdir("/Users/mac/Documents/GitHub/PythonDrill"):
        if file.endswith(".txt"):
            fName = os.path.join(fPath, file)
            endTime = os.path.getmtime(fName)
            print(file, endTime)



if __name__ == "__main__":
    findTxt()