import glob
import os
from unittest.util import unorderable_list_difference
import click
from os import listdir
import subprocess

#important file Assembly-CSharp.csproj


def getUnityVersion():
        global UnityPath
        editorName= []
        fileRoot = []
        counter = 0
        for x in os.listdir("C:/Program Files/Unity/Hub/Editor/"):
            editorName.extend(str(x) + " = " + str(counter))
            fileRoot.append('"C:/Program Files/Unity\Hub\Editor/'+ str(x) + '/Editor/Unity.exe"')
            print(str(x) + " = " + str(counter))
            counter = counter + 1
        UnityVersion = input("Select a Unity Version from the list Above: ")
        if UnityVersion != "":
            UnityPath = fileRoot[int(UnityVersion)]
        else:
            print("INVALID UNITY VERSION")
            menu(True)

def getGitFolder():
    global gitFolderHolder
    futureFolder = input("Input New Project Root: ")
    if futureFolder != "":
        gitFolderHolder = futureFolder
        print("Git Folder is!: " + futureFolder)
    else:
        print("Shutting Down....")
        menu(False)

def openFolder():
    printProjects()
    filePath = input("Input Project Root: ")
    if filePath != "":
        subprocess.Popen('cmd /c ' + UnityPath + " -projectPath " + filePath)
    else:
        print("Invalid Folder")

def buildGame():
    printProjects()
    filePath = input("Input Project Root: ")
    if filePath != "":
        buildFilePath = input("Input Folder for Build: ")
        if filePath != "":
            subprocess.Popen('cmd /c ' + UnityPath + " -projectPath " + filePath + " -buildWindows64Player" + buildFilePath)
    else:
        print("Invalid Folder")

def printProjects():
        if len(gitFolderHolder)!=0:
            for ref in gitFolderHolder:
                ref = ref.strip('\n')
                for root, dirs, files in os.walk(ref):
                # select file name
                    for file in files:
                    # check the extension of files
                        if file.startswith('Assembly-CSharp.csproj'):
                            print(os.path.join(root))

def menu(firstTime):
    global UnityPath
    global gitFolderHolder
    if firstTime == True:
        print("\n\nMinimal Unity Hub V0.1")
        getUnityVersion()
    else:
        print("\n\n")
    goal = input("1 to Create a new Project, 2 to Open a existing One, 3 to change Unity Versions, DEBUG for stats, anything else to quit: ")
    if goal == "1":
        filePath = input("Input New Project Root: ")
        os.system('cmd /c ' + UnityPath + " -createProject " + filePath)
        menu(False)
    elif goal == "2":
        openFolder()
        menu(False)
    elif goal == "3":
        getUnityVersion()
        menu(False)
    elif goal == "4":
        buildGame()
        menu(False)
    elif goal == "DEBUG":
        print("STATS: \nCurrent Editor:\n" + UnityPath + "\nCurrent Git Project Folders:")
        for ref in gitFolderHolder:
            ref = ref.strip('\n')
            print(ref)
        print("\nCurrent Projects")
        printProjects()
        menu(False)
    else:
        print("Shutting Down....")
        quit


if __name__ == "__main__":
    global UnityPath
    global gitFolderHolder
    gitFolderHolder = ''
    file1 = open('myGitFolders.txt', 'r')
    gitFolderHolder = file1.readlines()
    file1.close()
    UnityPath = '' 
    menu(True)