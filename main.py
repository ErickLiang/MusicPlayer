import tkinter
import pygame

from musicListFrame import MusicListFrame
from functionFrame import FunctionFrame

def main():

    musicResoucePath = r'E:\CloudMusic'
    mainWin = tkinter.Tk()
    mainWin.title('music player')
    mainWin.geometry('600x400+500+40')

    musicListFrame = MusicListFrame(mainWin, musicResoucePath)
    functionFrame = FunctionFrame(mainWin)

    mainWin.mainloop()

if __name__ == '__main__':
    main()