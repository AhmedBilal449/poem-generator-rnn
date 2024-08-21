import random
import numpy as np
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Activation
from keras.optimizers import RMSprop

filepath = tf.keras.utils.get_file ('shakespear.txt' , 'https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt')

text = open(filepath, 'rb').read().decode(encoding = 'utf-8').lower()

#If the program takes too long use this to limit the amount of text used to train the model.
#text = text[100000:300000]

characters = sorted(set(text))

char_to_index = dict((c , i) for i , c in enumerate(characters))
index_to_char = dict((i , c) for i , c in enumerate(characters))

SEQ_LENGTH = 40
STEP_SIZE = 3

sentences = []
next_characters = []

for i in range(0 , len(text) - SEQ_LENGTH , STEP_SIZE):
  sentences.append(text[i : i+SEQ_LENGTH])
  next_characters.append(text[i+SEQ_LENGTH])


