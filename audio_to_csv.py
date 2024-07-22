# conda activate AUDIOLIBROSA

import csv, numpy, librosa
import pandas as pd

list_of_wav_file_path = ['611.wav','611wm.wav']

def wav2csv(wavlist):
	for wav in wavlist:
		audio, _ = librosa.load(wav)
		numpy.savetxt(f"{wav[:-4]}.csv", audio, delimiter="\n") 

if __name__ == "__main__":
	wav2csv(list_of_wav_file_path)