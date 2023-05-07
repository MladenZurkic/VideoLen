import datetime
import os


def with_moviepy(filename):
    from moviepy.editor import VideoFileClip
    clip = VideoFileClip(filename)
    duration       = clip.duration
    return int(duration)


if __name__ == '__main__':
    extensions = ('.mp4', '.flv', '.webm', '.mkv', 'vob', '.avi', '.m4v')
    dirc = input("input directory: ")
    print("Searching for most popular video formats..")
    filenames= os.listdir(dirc)
    totalSeconds = 0

    for filename in filenames:
        if(filename.lower().endswith(extensions)):
            print(filename)
            seconds = with_moviepy(dirc + '\\' + filename)
            totalSeconds += seconds
            print(str(datetime.timedelta(seconds=seconds)))
            print("\n")
    print("Total duration: " + str(datetime.timedelta(seconds=totalSeconds)))

    input("Press enter to exit")