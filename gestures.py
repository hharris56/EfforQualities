# Hunter Harris
# October 25, 2020

# imports

# system
import os

# ml
import numpy
import pandas as pd
import tensorflow as tf
import csv
from keras.models import Sequential
from keras.layers import Dense

def main():

    # tf.get_logger().setLevel('FATAL')

    dataDir = "imgs"
    imgCount = sum([len(files) for r, d, files in os.walk("imgs")])
    imgWidth = 75
    imgHeight = 83

    train_dataset = 
    tf.keras.preprocessing.image_dataset_from_directory(
        dataDir,
        validation_split=0.2,
        subset="training",
        seed=420,
        image_size=(imgHeight, imgWidth),
        batch_size=imgCount
    )

    validation_dataset = 
    tf.keras.preprocessing.image_dataset_from_directory(
        dataDir,
        validation_split=0.2,
        subset="validation",
        seed=420,
        image_size=(imgHeight, imgWidth),
        batch_size=imgCount
    )

    train_dataset.cache().shuffle(100)
    validation_dataset.cache()

    # create and train model
    model = get_compiled_model()
    # model.fit(train_dataset, epochs=15)

def get_compiled_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(1)
    ])
    model.compile(
        optimizer='adam', 
        loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
        metrics=['accuracy'])
    return model


if __name__ == "__main__":
    main()