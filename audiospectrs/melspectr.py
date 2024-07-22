# https://blog.paperspace.com/music-genre-classification-using-librosa-and-pytorch/
# https://huggingface.co/learn/audio-course/ru/chapter1/audio_data

# conda activate AUDIOLIBROSA

import os
import numpy
import librosa
from matplotlib import pyplot

def get_mfcc(wav_file_path):
	'''
	коэффициенты, вычисляемые с помощью дискретного косинусоидального преобразования,
	применяемого к спектру мощности сигнала. Полосы частот этого спектра расположены
	логарифмически в соответствии со шкалой Mel.
	'''
	y, sr = librosa.load(wav_file_path, offset=0, duration=30)
	mfcc = numpy.array(librosa.feature.mfcc(y=y, sr=sr))
	return mfcc

def get_melspectrogram(wav_file_path):
	'''
	спектрограммa в шкале Mel, которая представляет собой шкалу восприятия звуков, 
	которые, по мнению слушателей, находятся на равном расстоянии друг от друга. 
	'''
	y, sr = librosa.load(wav_file_path, offset=0, duration=30)
	melspectrogram = numpy.array(librosa.feature.melspectrogram(y=y, sr=sr))
	return melspectrogram

def get_chroma_vector(wav_file_path):
	'''
	Вектор цветовых характеристик строится путем проецирования полного спектра на 12 ячеек, 
	которые отражают 12 уникальных полутонов (или цветовых оттенков) музыкальной октавы: 
	C, До#, Ре, D#, E, F, F#, G, G#, A, A#, B. Эта проекция обеспечивает интригующее и 
	мощное представление музыкального звука и особенно зависит от музыкального жанра.

	Поскольку ноты, отстоящие друг от друга ровно на одну октаву, воспринимаются как особенно 
	похожие в музыке, понимание распределения цветности, даже без знания абсолютной частоты 
	(т.е. исходной октавы), может предоставить полезную музыкальную информацию об аудиозаписи 
	и даже выявить кажущиеся музыкальные сходства в одном и том же музыкальном жанре, которые 
	не являются таковыми. видимый в исходных спектрах.
	'''
	y, sr = librosa.load(wav_file_path)
	chroma = numpy.array(librosa.feature.chroma_stft(y=y, sr=sr))
	return chroma

def get_tonnetz(wav_file_path):
	'''
	Это представление рассчитывается путем проецирования цветовых характеристик 
	на 6-мерную основу, представляющую идеальную квинту, малую терцию и большую 
	терцию в виде двумерных координат.
	'''
	y, sr = librosa.load(wav_file_path)
	tonnetz = numpy.array(librosa.feature.tonnetz(y=y, sr=sr))
	return tonnetz

def get_frequency_amplitude_db(wav_file_path):
	'''
	Другим способом визуализации аудиоданных является построение частотного спектра аудиосигнала, 
	также известное как частотный интервал. Спектр вычисляется с помощью Дискретного Преобразования 
	Фурье или ДПФ (Discrete Fourier Transform - DFT). Он описывает отдельные частоты, из которых 
	состоит сигнал, и их силу.
	'''

	y, sampling_rate = librosa.load(wav_file_path)
	dft_input = y[:4096]

	# Рассчитаем ДПФ
	window = numpy.hanning(len(dft_input))
	windowed_input = dft_input * window
	dft = numpy.fft.rfft(windowed_input)

	# получим амплитудный спектр в децибелах
	amplitude = numpy.abs(dft)
	amplitude_db = librosa.amplitude_to_db(amplitude, ref=numpy.max)

	# получим частотные столбцы
	frequency = librosa.fft_frequencies(sr=sampling_rate, n_fft=len(dft_input))

	return frequency, amplitude_db


example_file = "611wm.wav"

mfcc = get_mfcc(example_file)
pyplot.imshow(mfcc, interpolation='nearest', aspect='auto')
pyplot.title(f'Mel Frequency Cepstral Coefficients of {example_file}')
pyplot.show()

melspectrogram = get_melspectrogram(example_file)
pyplot.imshow(melspectrogram, interpolation='nearest', aspect='auto')
pyplot.title(f'Mel Spectrogram of {example_file}')
pyplot.show()

chroma = get_chroma_vector(example_file)
pyplot.imshow(chroma, interpolation='nearest', aspect='auto')
pyplot.title(f'Chroma Vector of {example_file}')
pyplot.show()

tntz = get_tonnetz(example_file)
pyplot.imshow(tntz , interpolation='nearest', aspect='auto')
pyplot.title(f'Tonal Centroid Features (Tonnetz) of {example_file}')
pyplot.show()

frequency_amplitude_db = get_frequency_amplitude_db(example_file)
pyplot.figure()
pyplot.plot(frequency_amplitude_db)
pyplot.xlim(0.1, 1)
pyplot.ylim([numpy.min(frequency_amplitude_db[1]), numpy.max(frequency_amplitude_db[1])])
pyplot.xlabel("Frequency (Hz)")
pyplot.ylabel("Amplitude (dB)")
pyplot.xscale("log")
pyplot.title(f'Frequency-amplitude_db of {example_file}')
pyplot.show()