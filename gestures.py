# Hunter Harris
# October 25, 2020

# imports

# system
import os
from PIL import Image

# ml
import numpy
import pandas as pd
import tensorflow as tf
import csv
from keras.models import Sequential
from keras.layers import Dense

effort_dict = {
    'float': 0,
    'punch': 1,
    'press': 0,
    'glide': 0,
    'slash': 1,
    'wring': 0,
    'dab': 1,
    'flick': 1
}

def main():

    # tf.get_logger().setLevel('FATAL')

    dataDir = "imgs"
    imgCount = sum([len(files) for r, d, files in os.walk("imgs")])

    imgWidth, imgHeight = get_dimensions(dataDir)

    print("data length: {}".format(imgHeight))

    train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        dataDir,
        validation_split=0.2,
        subset="training",
        seed=420,
        image_size=(imgHeight, imgWidth),
        batch_size=imgCount
    )

    validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
        dataDir,
        validation_split=0.2,
        subset="validation",
        seed=420,
        image_size=(imgHeight, imgWidth),
        batch_size=imgCount
    )

    # labels = train_dataset.class_names
    # for batch in train_dataset:
    #     for i in range(len(batch[1])):
    #         batch[1][i] = effort_dict[labels[batch[1][i]]]
    #         print(batch[1][i])
    #     # print(len(val[0]))

    train_dataset.cache().shuffle(100)
    validation_dataset.cache()

    # create and train model
    model = get_compiled_model()
    model.fit(
        train_dataset,
        validation_data=validation_dataset,
        epochs=15
        )
    # model.summary()

def get_compiled_model():
    model = tf.keras.Sequential([
        tf.keras.layers.experimental.preprocessing.Rescaling(1./255),
        tf.keras.layers.Conv2D(16, 3, padding='same', activation='relu'),
        tf.keras.layers.MaxPooling2D(),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(128, activation='relu')


        # tf.keras.layers.Dense(10, activation='relu'),
        # tf.keras.layers.Dense(10, activation='relu'),
        # tf.keras.layers.Dense(1)
    ])
    model.compile(
        optimizer='adam', 
        loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True),
        metrics=['accuracy'])

    return model

def get_dimensions(datadir):
    for direct in os.listdir(datadir):
        path = datadir + "/" + direct
        for imgFile in os.listdir(path):
            img = Image.open(path + "/" + imgFile)
            # DOESNT HAVE TO BE MINIMUM
            # ALL IMAGES ARE SET SIZE AT THIS POINT    
            return img.size

if __name__ == "__main__":
    main()
