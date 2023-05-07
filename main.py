import datetime
import os

def with_moviepy(filename):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(filename)
    duration       = clip.duration
    clip.close()
    return int(duration)


def getDurationForDirectory(path, level):
    filenames = os.listdir(path)
    first = True
    subtotalSeconds = 0
    totalSeconds = 0
    for filename in filenames:
        if(os.path.isdir((path + "\\" + filename))):
            nextPath = (path + "\\" + filename)
            totalSeconds += getDurationForDirectory(nextPath, level+1)


        if(filename.lower().endswith(extensions)):
            if(first):
                index = path.rfind("\\")
                print("\t" * (level - 1) + path[index + 1:])
                first = False
            print("\t" * (level-1) + "├──" +  filename[:40] + "...  - ", end="")
            seconds = with_moviepy(path + '\\' + filename)
            subtotalSeconds += seconds
            totalSeconds += seconds
            print(str(datetime.timedelta(seconds=seconds)), end="\n")
    if(not first):
        print("\t" * (level-1) + "Subtotal: " + str(datetime.timedelta(seconds=subtotalSeconds)))
    return totalSeconds



if __name__ == '__main__':
    extensions = ('.mp4', '.flv', '.webm', '.mkv', 'vob', '.avi', '.m4v')
    allDirs = 0
    dirc = input("input directory: ")
    # allDirs = input("Search all subfolders(1) or only this directory(0)? ")
    print("Searching for most popular video formats..")

    total = getDurationForDirectory(dirc, 1)

    print("TOTAL: " +str(datetime.timedelta(seconds=total)))