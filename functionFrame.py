import tkinter

class FunctionFrame():
    def __init__(self, master):
        self.frame = tkinter.Frame(master)
        self.frame.grid(row=0, column=1)

        # play button
        self.playButton = tkinter.Button(self.frame, text='Play', width=15, command=self.play)
        self.playButton.grid(row=0, column=0)
        # self.playButton.pack(side=tkinter.LEFT)

        # pause button
        self.pauseButton = tkinter.Button(self.frame, text='Pause', width=15, command=self.pause)
        self.pauseButton.grid(row=0, column=1)
        # self.pauseButton.pack(side=tkinter.RIGHT)

        # stop button
        self.stopButton = tkinter.Button(self.frame, text='Stop', width=15, command=self.stop)
        self.stopButton.grid(row=0, column=2)

        # last song button
        self.lastSongButton = tkinter.Button(self.frame, text='Last', width=15, command=self.lastSong)
        self.lastSongButton.grid(row=1, column=0)

        # next song button
        self.nextSontButton = tkinter.Button(self.frame, text='Next', width=15, command=self.netxSong)
        self.nextSontButton.grid(row=1, column=1)

        # exit button
        self.exitButton = tkinter.Button(self.frame, text='Exit', width=15, command=tkinter._exit)
        self.exitButton.grid(row=1, column=2)

    def play(self):
        pass

    def stop(self):
        pass

    def pause(self):
        pass

    def nextSong(self):
        pass

    def lastSong(self):
        pass