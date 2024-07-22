# https://www.geeksforgeeks.org/python-pearson-correlation-test-between-two-variables/

# Import those libraries
import pandas as pd
from scipy.stats import pearsonr

from audio_to_csv import wav2csv
from merge_csv import merge_audio_csv

audio1 = '611.wav'
audio2 = '611wm.wav'

list_of_wav_file_path = [audio1, audio2]


wav2csv(list_of_wav_file_path)
merge_audio_csv(f"{audio1[:-4]}.csv", f"{audio2[:-4]}.csv")


df = pd.read_csv("audios.csv")
# Convert dataframe into series
list1 = df['0']
list2 = df['1']

# Apply the pearsonr()
corr, _ = pearsonr(list1, list2)
print('Pearsons correlation: %.6f' % corr) # 0.999710