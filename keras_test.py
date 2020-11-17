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

    minLength = 82

    inputSet = []
    labelSet = []

    # get each file
    dirpath = "{}/dataset".format(os.getcwd())
    print(dirpath)
    filenames = os.listdir(dirpath)
    for i in range(len(filenames)):
            
        fileInput = pd.read_csv("{}/{}".format(dirpath, filenames[i]), header=None, sep=',')
        fileLabel = fileInput.tail(1).dropna('columns', 'any')
        fileInput = fileInput.truncate(before=0, after=minLength)
        fileInput['target'] = fileLabel[0]
        # fileInput.drop(fileInput.tail(1).index, inplace=True)

        dataSet = tf.data.Dataset.from_tensor_slices((fileInput, fileLabel))

        return 0
        # inTensor = tf.constant(fileInput, dtype=tf.float16)
        # outTensor = tf.constant(fileLabel, dtype=tf.int8)

        # print(inTensor)
        # print(outTensor)

        # print(fileInput)
        # print(fileLabel)

        inputSet.append(inTensor)
        labelSet.append(outTensor)
    
    # " At this point we have aggregated our data from files into tensors "

    # convert array of tensors into a tensor
    tf.convert_to_tensor(inputSet)
    tf.convert_to_tensor(labelSet)

    # train_dataset = dataset.shuffle(len(dataset)).batch(1)

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