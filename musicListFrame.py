import os
import tkinter
from tkinter import ttk

class MusicListFrame():
    def __init__(self, master, musicResoucePath):
        self.frame = tkinter.Frame(master)
        self.frame.grid(row=0, column=0)

        self.tree = ttk.Treeview(self.frame)
        self.tree.pack()
        root = self.tree.insert('', 'end', text=self.getMusicList(musicResoucePath), open=True)

        self.loadSong(root, musicResoucePath)

    def getMusicList(self, musicResoucePath):
        return os.path.split(musicResoucePath)[-1]

    def loadSong(self, root, path):
        subPath = os.path.join(path)
        for fileName in os.listdir(subPath):
            treey = self.tree.insert(root, 'end', text=fileName)