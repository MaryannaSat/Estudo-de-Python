print('Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.')
'''import playsound
'''
playsound.mixer.init()
playsound.mixer.music.load('pintinho.mp3')
playsound.mixer.music.play()
playsound.event.wait()'''
Deu problema'''

'''from pygame import mixer, event
import time
import eyed3
musica = input('')
t = eyed3.load(musica).info.time_secs
mixer.init()
mixer.music.load(musica)
mixer.music.play()
time.sleep(t)'''
'''pip playsound install
from playsound import playsound
playsound('pintinho.mp3')'''