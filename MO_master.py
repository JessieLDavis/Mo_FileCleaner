import os, copy
from random import choice

#STEP 1: Update path locations to needed locations.

#Only full paths have been tested
sourceFile = "" #The path to the top file to scan

#all following files should be located OUTSIDE the source file folder to prevent unneccessary looping.
destinationFile = "" #The default path for files to move. "MusicDive" = any listed song or movie files. "MegaDive" = listed movie and gif files that do not easily fit elsewhere
problemDiving = "" #If there is a duplicate when "MusicDive" attempts to move to the destinationFile, it will attempt to move to this file.
pdfPath = "" #The default path for pdfs to move in the "MusicDive". On "MegaDive", this file also will hold .doc and .docx files.
picPath = "" #The default path for "MegaDive" to move common picture file types.
vidPath = "" #The default path for "MegaDive" to move common video file types. Some may end up in the destination file.
psdPath = "" #The default path for "MegaDive" to move psd (Photoshop) files.
stlPath = "" #The default path for "MegaDive" to move stl (3D print models) files.
rhinoPath = "" #The default path for "MegaDive" to move .3dm files (Rhinocerous3D). This could be multipe file types

fileTrash = "" #The default path for "CheckFolderContents" to move the file to if confirmed.

#If wanting to test, uncomment the next line. Caution! There is no reset.
# sourceFile, destinationFile, problemDiving, pdfPath, picPath, vidPath, psdPath, stlPath, rhinoPath, fileTrash = "Test_Example/sourceFile","Test_Example/destinationFile","Test_Example/problemDiving","Test_Example/pdfPath","Test_Example/picPath","Test_Example/vidPath","Test_Example/psdPath","Test_Example/stlPath","Test_Example/rhinoPath","Test_Example/fileTrash"

fileList = [folder for folder in os.listdir(sourceFile)]

def musicDive(fileList,sourceFile):
    for file in fileList: #Iterating over a copy of the fileList.
        if file.endswith(".mp4") or file.endswith(".wma") or file.endswith(".m4v") or file.endswith(".wav") or file.endswith(".WAV") or file.endswith(".m4a") or file.endswith(".M4A") or file.endswith(".wma") or file.endswith(".WMA") or file.endswith(".mp3") or file.endswith(".MP3"):
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(destinationFile,file)
            try:
                os.rename(fileExists,fileDestination)
                print(f"{file} moved")
            except FileExistsError:
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False: #Will try to move up to 15 times. Breaks if the counter reaches 15 duplicates.
                    try:
                        fileDestination = os.path.join(problemDiving,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
            # print(f"{file} moved")
            # pause = input("----")
        elif file.endswith(".jpg"):
            pass
        elif file.endswith(".pdf"):
            fileExists= os.path.join(sourceFile,file)
            fileDestination = os.path.join(pdfPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
            except FileExistsError:
                print("file exists")
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(pdfPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        else:
            try:
                sourceFilePlus = os.path.join(sourceFile,file)
                deepFile = [folder for folder in os.listdir(sourceFilePlus)]
                copyDeepFile = copy.deepcopy(deepFile)
                musicDive(copyDeepFile,sourceFilePlus) #If there is no match for any of the specified file tags, it will automatically try to recursively dive into the file.
            except:
                print("problem diving")
                print(sourceFilePlus)


def megaDive(fileList, sourceFile):
    for file in fileList:
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".petg") or file.endswith(".JPG") or file.endswith(".tif"):
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(picPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(picPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        elif file.endswith(".stl"):
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(stlPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(stlPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        elif file.endswith(".3dm"):
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(rhinoPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(rhinoPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        elif file.endswith(".mov") or file.endswith(".m4a") or file.endswith(".mp4"):
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(vidPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(vidPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        elif file.endswith(".gif") or file.endswith(".mp4") or file.endswith(".wma") or file.endswith(".m4v") or file.endswith(".wav") or file.endswith(".WAV") or file.endswith(".m4a") or file.endswith(".M4A") or file.endswith(".wma") or file.endswith(".WMA") or file.endswith(".mp3") or file.endswith(".MP3"):
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(destinationFile,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(destinationFile,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        elif file.endswith(".pdf") or file.endswith(".doc") or file.endswith("docx"):
            fileExists= os.path.join(sourceFile,file)
            fileDestination = os.path.join(pdfPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                print("file exists")
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(pdfPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        elif file.endswith(".psd") or file.endswith(".ai"):
            fileExists= os.path.join(sourceFile,file)
            fileDestination = os.path.join(psdPath,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
                print(f"{file} moved")
            except FileExistsError:
                print("file exists")
                renameWorked = False
                print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(psdPath,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 15:
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        else:
            try:
                sourceFilePlus = os.path.join(sourceFile,file)
                deepFile = [folder for folder in os.listdir(sourceFilePlus)]
                copyDeepFile = copy.deepcopy(deepFile)
                megaDive(copyDeepFile,sourceFilePlus) #If there is no match for any of the specified file tags, it will automatically try to recursively dive into the file.
            except:
                print("problem diving")
                print(sourceFilePlus)

def checkEmpty(fileList,sourceFile): #A quick recursive loop to display everything in the specified file. See Row 280.
    for file in fileList:
        print(file)
        try:
            sourceFilePlus = os.path.join(sourceFile,file)
            deepFile = [folder for folder in os.listdir(sourceFilePlus)]
            copyDeepFile = copy.deepcopy(deepFile)
            checkEmpty(copyDeepFile,sourceFilePlus)
            print("-")
        except:
            pass

def checkFolderContents(fileList):
    fileListCopy = copy.deepcopy(fileList)
    for file in fileListCopy:
        print("~~~~~~~~~~~~~~~~\n")
        sourceFilePlus = os.path.join(sourceFile,file)
        deepFile = [folder for folder in os.listdir(sourceFilePlus)]
        deepfileCopy = copy.deepcopy(deepFile)
        checkEmpty(deepfileCopy,sourceFilePlus)
        confirmTrash = input(f"Would you like to move {file} to temp trash? y/n\n>  ") #After showing all the elements of a file in the console, asks for confirmation to move to the trash file.
        if confirmTrash == "y" or confirmTrash == "Y":
            fileExists = os.path.join(sourceFile,file)
            fileDestination = os.path.join(fileTrash,file)
            try:
                os.rename(fileExists,fileDestination)
                renameWorked = True
            except FileExistsError:
                print("file exists")
                renameWorked = False
                # print("file exists")
                counter = 0
                while renameWorked == False:
                    try:
                        fileDestination = os.path.join(fileTrash,f"(COPY {counter})"+file)
                        os.rename(fileExists,fileDestination)
                        renameWorked = True
                        print(f"{file} moved")
                    except FileExistsError:
                        if counter > 50: # It will try to move to the Trash file 50 times. If there is still a duplicate, it will break the loop.
                            renameWorked = True
                        else:
                            renameWorked = False
                            counter += 1
        else:
            pass

def runSearch(fileList,choice): #Not fully tested
    fileListCopy = copy.deepcopy(fileList)
    try:
        choice = int(choice)
    except:
        choice = "error"
    if choice == 1:
        musicDive(fileListCopy,sourceFile)
    elif choice == 2:
        megaDive(fileListCopy,sourceFile)
    elif choice == 3:
        checkFolderContents(fileList)
    elif choice == 4:
        print("Goodbye!")
        return
    else:
        print("Invalid choice. Please try again.")
        choice = input("Please choose a program to run. \n1 = musicDive\n2 = megaDive\n3 = checkFolderContents\n4 = Quit\n>  ")
        return runSearch(fileList,choice)

#STEP 2: Run File
if __name__ is "__main__": #Not fully tested
    confirmGo = input("Please confirm that all file locations match expectations. If needed restart. \nOtherwise press enter to continue.")
    choice = input("Please choose a program to run. \n1 = musicDive\n2 = megaDive\n3 = checkFolderContents\n4 = Quit\n>  ")
    runSearch(fileList,choice)

