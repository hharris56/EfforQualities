# Hunter Harris
# October 25, 2020

# imports

# system
import os

# ml
import numpy
import pandas as pd
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

def main():
    # inputSet = numpy.array((75,1,1))
    # labelSet = numpy.array((1,1,1))
    inputSet = pd.DataFrame()
    labelSet = pd.DataFrame()

    # get each file
    dirpath = "{}/dataset".format(os.getcwd())
    print(dirpath)
    filenames = os.listdir(dirpath)
    for i in range(len(filenames)):
        fileInput = pd.read_csv("{}/{}".format(dirpath, filenames[i]), header=None, sep=',')
        fileLabel = fileInput.tail(1).dropna('columns', 'any')
        fileInput.drop(fileInput.tail(1).index, inplace=True)
        # print(fileInput)
        # print(fileLabel)

        inputSet = inputSet.append(fileInput)
        labelSet = labelSet.append(fileLabel, ignore_index=True)
    
    # " At this point we have aggregated our data from files "

    # turn data into a Dataset, shuffle and batch
    dataset = tf.data.Dataset.from_tensor_slices(inputSet)
    for element in dataset:
        print(element)

    return 0
    train_dataset = dataset.shuffle(len(dataset)).batch(1)

    # create and train model
    model = get_compiled_model()
    model.fit(train_dataset, epochs=15)

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