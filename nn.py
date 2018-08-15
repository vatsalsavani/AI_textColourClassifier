import tensorflow as tf
import csv

# Dataset creation and editing
# Output class identification : [black, white]

# Loading and setting up the dataset
datasetFile = open('./dataset.csv', 'r')
reader = csv.reader(datasetFile)
dataset = []

# Formatting dataset to suit our needs for this NeuralNet


def hex_to_rgb(hex):
    hex = hex.lstrip('#')
    hLen = len(hex)
    return tuple(int(hex[i:i+hLen/3], 16) for i in range(0, hLen, hLen/3))


for row in reader:
    row[0] = hex_to_rgb(row[0])

    if row[1] == 0:
        row[1] = [1, 0]
    else:
        row[1] = [0, 1]

    dataset.append(row)

print(dataset)
