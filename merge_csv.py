import csv
import pandas as pd 

audio1 = '611.csv'
audio2 = '611wm.csv'

def merge_audio_csv(audio1, audio2):
    data1 = pd.read_csv(audio1)
    data2 = pd.read_csv(audio2) 
    output1 = pd.concat([data1, data2], axis=1, ignore_index=True) 
    output1 = output1.iloc[1: , :]
    output1.to_csv("audios.csv", index=False)

if __name__ == "__main__":
    merge_audio_csv(audio1, audio2)