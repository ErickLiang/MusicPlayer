import os
import tkinter
from tkinter import ttk

class MusicListFrame():
    def __init__(self, master, musicResoucePath):
        # 增加左侧frame，为歌单显示
        self.frame = tkinter.Frame(master)
        self.frame.grid(row=0, column=0)

        # 新的树
        self.tree = ttk.Treeview(self.frame)
        self.tree.pack(side=tkinter.LEFT, fill=tkinter.Y)
        root = self.tree.insert('', 'end', text=self.getMusicList(musicResoucePath), open=True)

        # 增加分支
        self.loadSong(root, musicResoucePath)

        # 增加滚动条
        self.scrollbar = tkinter.Scrollbar(self.frame)
        self.scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.scrollbar.config(command=self.tree.yview)

        self.tree.config(yscrollcommand=self.scrollbar.set)

        # 绑定事件：分支选中，
        self.tree.bind("<<TreeviewSelect>>", self.getSelectedSong)

    # 返回被选中的值
    def getSelectedSong(self, event):
        self.v = event.widget.selection()
        for sv in self.v:
            file = self.tree.item(sv)['text']
            print(file)
            return file

    # 路径处理，作为分支的值显示
    def getMusicList(self, musicResoucePath):
        return os.path.split(musicResoucePath)[-1]

    def loadSong(self, root, path):
        subPath = os.path.join(path)
        for fileName in os.listdir(subPath):
            treey = self.tree.insert(root, 'end', text=fileName)