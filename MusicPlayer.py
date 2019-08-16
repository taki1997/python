import os
import pygame

def welcome():
    print('''
    *************************
    * 欢迎来到酷我音乐播放器 *
    *************************
    ''')

def select():
    print('''
    **************************
    * 1.播放       2.停止     *
    * 3.下一曲     4.上一曲   *
    * 5.增大音量   6.减少音量 *
    *      0.退出             *
    ***************************
    ''')
    return input("请选择您要操作的选项：")


def getMusicList(path):
    fileList = os.listdir(path)
    musicList = []
    for filename in fileList:
        musicList.append(os.path.join(path,filename))
    return musicList

def playMusic(path):
    pygame.mixer.init()
    pygame.mixer.music.load(path)
    pygame.mixer.music.play()

def nextMusic(musicList,index):
    # if index >= len(musicList)-1:
    #     print("已经是最后一首了")
    #     return index
    # else:
    #     index += 1
    # playMusic(musicList[index])
    # return index
    index += 1
    playMusic(musicList[index%len(musicList)])
    return index



if __name__ == '__main__':
    welcome()
    path = r"D:\music"
    musicList = getMusicList(path)
    index = 0
    while True:
        num = select()
        if num == "1":
            print("播放")
            playMusic(musicList[index])
        elif num == "2":
            print("暂停")
        elif num == "3":
            print("下一首")
            index = nextMusic(musicList,index)
        elif num == "4":
            print("上一首")
        elif num == "5":
            print("增大音量")
        elif num == "6":
            print("减少音量")
        elif num == "0":
            print("退出")
            break
        else:
            print("选择有误，请重新选择...")


