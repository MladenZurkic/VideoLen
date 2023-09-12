import datetime
import os

def with_moviepy(filename):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(filename)
    duration       = clip.duration
    clip.close()
    return int(duration)


def checkAllSubfolders(path):
    filenames = os.listdir(path)
    for filename in filenames:
        if(os.path.isdir((path + "\\" + filename))):
            return checkAllSubfolders(path + "\\" + filename)
        if(filename.lower().endswith(extensions)):
            return True
    return False

def getDurationForDirectory(path, level):
    filenames = os.listdir(path)
    first = True
    subtotalSeconds = 0
    totalSeconds = 0
    for filename in filenames:
        if(os.path.isdir((path + "\\" + filename))):
            nextPath = (path + "\\" + filename)

            #check all subfolders for videos
            #if(not checkAllSubfolders(nextPath)):
               # continue

            print('\033[1m' + os.path.basename(path))
            print( "\t" * (level - 1) + "└──", end="")
            totalSeconds += getDurationForDirectory(nextPath, level+1)


        if(filename.lower().endswith(extensions)):
            if(first):
                index = path.rfind("\\")
                print('\033[1m' + path[index + 1:])
                first = False
            stringTest = '\033[0m' + "\t" * (level-1) + "├──" +  filename[:40] + "...  - "
            print(f'{stringTest:<50}', end="")
            seconds = with_moviepy(path + '\\' + filename)
            subtotalSeconds += seconds
            totalSeconds += seconds
            print(str(datetime.timedelta(seconds=seconds)), end="\n")
    if(not first):
        print('\033[1m' + "\t" * (level-1) + "Subtotal: " + str(datetime.timedelta(seconds=subtotalSeconds)))
        print('\033[0m')
    return totalSeconds



if __name__ == '__main__':
    extensions = ('.mp4', '.flv', '.webm', '.mkv', 'vob', '.avi', '.m4v')
    allDirs = 0
    allTotal = 0
    while(True):
        dirc = input("input directory: ")
        if(dirc == ""):
            exit(0);
        # allDirs = input("Search all subfolders(1) or only this directory(0)? ")

        print("Searching for most popular video formats..\n")
        total = getDurationForDirectory(dirc, 1)
        allTotal += total;
        print('\033[1m')
        print(f'{"TOTAL:":<11}' +str(datetime.timedelta(seconds=total)))
        print(f'{"ALL TOTAL: ":<11}' + str(datetime.timedelta(seconds=allTotal)))
        print('\033[0m')