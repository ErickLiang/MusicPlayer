from pygame import mixer

class MusicFunction():
    def __init__(self, songFile):
        self.songFile = songFile
        mixer.init()
        mixer.music.load(self.songFile)

    def play(self):
        mixer.music.play()

    def pause(self):
        mixer.music.pause()

    def stop(self):
        mixer.music.stop()

    def getPlayTime(self):
        pass