# Hunter Harris
# Deriving effort qualities using only wrist positions
# November 18, 2020

import tensorflow as tf
import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

filepath = "output.csv"

def main():

    # read in data
    mPositions = pd.read_csv(filepath)

    # assign label array
    mLabels = mPositions.transpose().tail(1).transpose()
    bLabels = mLabels != 0

    # drop label column
    mPositions = mPositions.transpose()
    mPositions.drop(mPositions.tail(1).index, inplace=True)
    mPositions = mPositions.transpose()

    print(bLabels)
    print(mPositions)

    model = get_compiled_model()

    model.fit(
        mPositions,
        bLabels,
        epochs=30
    )

    return 0


def get_compiled_model():
    tf.keras.backend.set_floatx('float64')
    model = tf.keras.Sequential([
        # tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
        # tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
        # tf.keras.layers.MaxPooling2D(),
        # tf.keras.layers.Flatten(),
        # tf.keras.layers.Dense(128, activation='relu')
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(128, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(
        optimizer='adam', 
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=['accuracy'])

    return model



if __name__ == "__main__":
    main()