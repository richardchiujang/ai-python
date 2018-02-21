# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 09:42:47 2018

@author: richardchiu
"""

import speech_recognition as sr
r = sr.Recognizer()
d = 15
i = 1
with sr.AudioFile("D:\\AI\\0003.wav") as source:
    
    while i < 31:
        audio = r.record(source ,duration=d, offset=0)
        try:
            print( i ,":", r.recognize_google(audio, language='zh-TW') ) 
            #print( i ,":", r.recognize_google(audio, language='zh-CN') ) 
            #print( i ,":", r.recognize_bing(audio, language='zh-TW') ) 
        except sr.UnknownValueError:
            print(i,":", "Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(i,":", "Could not request results from Google Speech Recognition service; {0}".format(e))    
        
        i += 1    
